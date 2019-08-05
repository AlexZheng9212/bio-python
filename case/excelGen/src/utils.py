def byte2dict(inputByte):
  convert = str(inputByte, encoding = "utf-8")
  convert = eval(convert)
  return convert

def dict2byte(inputDict):
  convert = bytes(str(inputDict),'utf-8')
  return convert

def getRequestBody(environ):
  request_method = environ['REQUEST_METHOD']
  if request_method == 'PUT':
    print('put todo')
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except (ValueError):
    request_body_size = 0
  request_body = environ['wsgi.input'].read(request_body_size)
  request_body = byte2dict(request_body)
  return request_body
