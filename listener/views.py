"""
GitHub webhook API handlers.
"""
from rest_framework.views import APIView
from rest_framework.response import Response


class PushListener(APIView):
    """
    Webhook listener for push action.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle GET request.
        """
        return Response()
