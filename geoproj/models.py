from django.db import models
from django.contrib.gis.db import models

class Air_Lidar(models.Model):
    location = models.CharField(max_length = 1000)
    coverage = models.FloatField()
    date_of_capture = models.DateField(auto_now= True)
    sensor_name = models.CharField(max_length = 250)
    data_density = models.FloatField()
    fva = models.CharField(max_length = 250)
    fha = models.CharField(max_length = 250)
    horizontal_datum = models.CharField(max_length = 250)
    map_projection = models.CharField(max_length = 250)
    vertical_datum = models.CharField(max_length = 250)
    geoid_model = models.CharField(max_length = 250)
    scan_angle = models.CharField(max_length = 250)
    track_point_spacing_ratio = models.CharField(max_length = 250)
    flight_overlap = models.FloatField()
    environmental_conditions = models.CharField(max_length = 250)
    intensity = models.BooleanField(default = False)
    intensity_value = models.FloatField()
    height_of_flight = models.FloatField()
    velocity_of_flight = models.FloatField()
    nature_of_aerial_platform = models.IntegerField() #put choices #edit
    horizontal_accuracy = models.CharField(max_length = 250)
    project_manager = models.CharField(max_length = 250)
    user_department = models.CharField(max_length = 250)
    # add a variable prf                  #edit
    multiple_returns = models.BooleanField(default = False)
    number_of_returns = models.FloatField()
    waveform_captured = models.BooleanField(default = False)
    kml_file = models.FileField()#edit
    poly = models.MultiPolygonField(dim = 2) # edit #what's extent attribute

    def __str__(self):
        return "%s Air Bourne Lidar data" %self.location


class Orthophoto(models.Model):
    name_ortho = models.CharField(max_length = 250)
    coverage = models.FloatField()
    data_source1 = models.ForeignKey(Air_Lidar, on_delete = models.SET_NULL , null = True, blank = True) #edit #remove cascade
    #data_source2 = models.ForeignKey('Mobile_Lidar', on_delete = models.SET_NULL , null = True, blank = True)
    #data_source3 = models.ForeignKey('Terrestrial_Lidar', on_delete = models.SET_NULL , null = True, blank = True)
    date_of_capture = models.DateField(auto_now= True)
    file_Format = models.CharField(max_length = 250) #add choices #edit
    gsd = models.FloatField()
    true_colour = models.BooleanField(default = True)
    false_colour = models.BooleanField(default = False)
    collection_condition = models.CharField(max_length = 1000)
    horizontal_datum = models.CharField(max_length = 250)
    vertical_datum = models.CharField(max_length = 250)
    geoid_model = models.CharField(max_length = 250)
    map_projection = models.CharField(max_length = 250)
    horizontal_accuracy = models.CharField(max_length = 250)
    radiometric_resolution = models.CharField(max_length = 250)
    orthorectification_technique = models.CharField(max_length = 250)


    """class Meta():
        abstract = True"""

    def __str__(self):
        return "%s Orthophoto, derived from %s lidar data" %(self.name_ortho, self.data_source1)  #edit"""




class DEM(models.Model):
    coverage = models.FloatField()
    date_of_capture = models.DateField(auto_now= True)
    grid_size = models.FloatField()
    vertical_Accuracy = models.CharField(max_length = 250)
    map_projection = models.CharField(max_length = 250)
    horizontal_datum = models.CharField(max_length = 250)
    vertical_datum = models.CharField(max_length = 250)
    file_Format = models.CharField(max_length = 250) #add choices #edit
    data_source1 = models.ForeignKey(Air_Lidar, on_delete = models.SET_NULL , null = True, blank = True) #edit
    #data_source2 = models.ForeignKey('Mobile_Lidar', on_delete = models.SET_NULL , null = True, blank = True)
    #data_source3 = models.ForeignKey('Terrestrial_Lidar', on_delete = models.SET_NULL , null = True, blank = True)
    kml_file = models.FileField()#edit
    poly = models.MultiPolygonField(dim = 2) # edit #what's extent attribute

    """class Meta():
        abstract = True"""

class Intensity_Image(models.Model):
    coverage = models.FloatField()
    date_of_capture = models.DateField(auto_now= True)
    pixel_size = models.FloatField()
    file_Format = models.CharField(max_length = 250)
    data_source1 = models.ForeignKey(Air_Lidar, on_delete = models.SET_NULL , null = True, blank = True) #edit
    #data_source2 = models.ForeignKey('Mobile_Lidar', on_delete = models.SET_NULL , null = True, blank = True)
    #data_source3 = models.ForeignKey('Terrestrial_Lidar', on_delete = models.SET_NULL , null = True, blank = True)
    radiometric_resolution = models.CharField(max_length = 250)
    method_of_interpolation = models.CharField(max_length = 250)

    """class Meta():
        abstract = True"""









   


