from django.db.backends.postgresql import base, features


class DatebaseFeatures(features.DatabaseFeatures):
    def allows_group_by_selected_pks_on_model(self, model):
        return True


class DatebaseWrapper(base.DatabaseWrapper):
    features_class = DatebaseFeatures


