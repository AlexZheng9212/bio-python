import utils
class AppClass:
  def __init__(self, environ, start_response, REQUESTBODY):
    self.environ = environ
    self.start = start_response
    self.REQUESTBODY = REQUESTBODY

  def __iter__(self):
    status = '200 OK'
    response_headers = [('Context-type','text/plain')]
    print('say hi')
    self.start(status,response_headers)
    print(self.REQUESTBODY)
    yield self.REQUESTBODY
  
def handler(environ, start_response):
  requestBody = utils.getRequestBody(environ)
  print(requestBody)
  requestBody = [{'a':'pppss','b':'ccc','c':'dd'},{'a':'pppss','b':'ccc','c':'dd'}]
  REQUESTBODY = utils.dict2byte(requestBody)
  return AppClass(environ, start_response, REQUESTBODY)