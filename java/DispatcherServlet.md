# DispatcherServlet

1. 사용자의 요청을 DispatcherServlet이 받는다.
2. 요청을 처리해야하는 컨트롤을 찾기위해 **HandlerMapping**에게 질의 하고 **HandlerMapping**은 컨트롤 객체에 매핑되어 있는 URL을 찾아낸다.

