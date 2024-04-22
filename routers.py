class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'tmp':
            return 'asd'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'tmp':
            return 'asd'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'tmp' or obj2._meta.app_label == 'tmp':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'tmp':
            return db == 'asd'
        return None
    




class DataRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'temp2':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'temp2':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'temp2' or obj2._meta.app_label == 'temp2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'temp2':
            return db == 'default'
        return None