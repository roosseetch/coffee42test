from django.db.models import get_model

RequestContent = get_model('chamber', 'RequestContent')


class RequestContentMiddleware(object):


	def process_response(self, request, response):
		request_log = RequestContent(
			method=request.method,
			path=request.path,
			status_code=response.status_code
		)
		request_log.save()
		return response
