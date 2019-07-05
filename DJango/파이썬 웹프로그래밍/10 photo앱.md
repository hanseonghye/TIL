# 10. photo 앱

### fields.py

```python
import os

from PIL import Image
from django.db.models.fields.files import ImageFieldFile, ImageField


def _add_thumb(s):
    parts = s.split('.')
    parts.insert(-1, 'thumb')

    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)

    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)

    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        )
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=123, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)

```

- ThumbnailImageField
  - ImageField를 상속받는다. 
  - FileField 클래스를 정의할 떄는 그에 상응하는 File 처리 클래스를 `attr_class`속성에 정의해야 한다.
- ThumbnailImageFieldFile
  - 파일 시스템에 직접 파일을 쓰고 지우는 작업을 한다.

