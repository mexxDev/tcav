class HParams(object):
    def __init__(self, model_type='linear', alpha=.01, max_iter=1000, tol=1e-3):
        self.model_type = model_type
        self.alpha = alpha
        self.max_iter = max_iter
        self.tol = tol