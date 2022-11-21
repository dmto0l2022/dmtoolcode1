
 __tablename__ = 'students'

class Experiments(models.Model):
    
     __tablename__ = 'students'
        
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiments'


class LimitDisplays(models.Model):
    limit_id = models.IntegerField(blank=True, null=True)
    plot_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_displays'


class LimitOwnerships(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    limit_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_ownerships'


class Limits(models.Model):
    spin_dependency = models.CharField(max_length=255, blank=True, null=True)
    result_type = models.CharField(max_length=255, blank=True, null=True)
    measurement_type = models.CharField(max_length=60, blank=True, null=True)
    nomhash = models.TextField(blank=True, null=True)
    x_units = models.CharField(max_length=255, blank=True, null=True)
    y_units = models.CharField(max_length=255, blank=True, null=True)
    x_rescale = models.CharField(max_length=255, blank=True, null=True)
    y_rescale = models.CharField(max_length=255, blank=True, null=True)
    default_color = models.CharField(max_length=255, blank=True, null=True)
    default_style = models.CharField(max_length=255, blank=True, null=True)
    data_values = models.TextField(blank=True, null=True)
    data_label = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    data_comment = models.CharField(max_length=255, blank=True, null=True)
    data_reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    experiment = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    date_of_announcement = models.DateField(blank=True, null=True)
    public = models.IntegerField(blank=True, null=True)
    official = models.IntegerField(blank=True, null=True)
    date_official = models.DateField(blank=True, null=True)
    greatest_hit = models.IntegerField(blank=True, null=True)
    date_of_run_start = models.DateField(blank=True, null=True)
    date_of_run_end = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limits'


class PlotOwnerships(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    plot_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plot_ownerships'


class Plots(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    x_min = models.CharField(max_length=255, blank=True, null=True)
    x_max = models.CharField(max_length=255, blank=True, null=True)
    y_min = models.CharField(max_length=255, blank=True, null=True)
    y_max = models.CharField(max_length=255, blank=True, null=True)
    x_units = models.CharField(max_length=255, blank=True, null=True)
    y_units = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    plot_png = models.TextField(blank=True, null=True)
    legend_png = models.TextField(blank=True, null=True)
    plot_eps = models.TextField(blank=True, null=True)
    legend_eps = models.TextField(blank=True, null=True)
    no_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plots'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SimpleCaptchaData(models.Model):
    key = models.CharField(max_length=40, blank=True, null=True)
    value = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simple_captcha_data'

