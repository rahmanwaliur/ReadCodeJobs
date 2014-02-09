from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

MEDCODES = [
	['2453', '526', '6254', '8264', '46252'],
	['6152', '8462', '4351', '9184', '6451'],
	['6452', '8676', '7562', '6452', '7563'],
	['5462', '9673', '7563', '6573', '7563']
]

class MedCodes(APIView):

	def get(self, requests):

		return Response(MEDCODES)
