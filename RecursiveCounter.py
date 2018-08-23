class RecursiveCounter:
    def __init__(self):
        self._count = 0
        self._invoker = None
        pass

    def _set_invoker(self, invoker_wrapper):
        self._invoker = lambda param: invoker_wrapper(self, *param)

    def invoke(self, *params):
        self._count += 1
        return self._invoker(params)

    def get_count(self):
        return self._count

    @staticmethod
    def create_recursive_counter(invoker_wrapper):
        counter = RecursiveCounter()
        counter._set_invoker(invoker_wrapper)
        return counter
