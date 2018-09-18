from flask_dance.contrib.github import make_github_blueprint, github

github_blueprint = make_github_blueprint(client_id='a66c37fc7dad55530d64', client_secret='adad4baefe1d6b2f090ff6be9098b145f7d41318')


from . import views, forms
