from webhook_app import models, create_app
models.db.create_all(app=create_app())