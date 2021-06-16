from .platform.eos import EOSViewSet

class ViewFactory:

    def __init__(self):
        self._views = {}
        self.register("vEOS",EOSViewSet)

    def register(self, platform, view):
        self._views[platform] = view

    def get_view(self, request,**initkwargs):
        for k in self._views:
            view = self._views[k](**initkwargs)
            if view.use_for_request(request):
                return view


        return None

