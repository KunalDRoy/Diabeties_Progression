from distutils.command.config import config
import pickle
import numpy as np
import json
import config

class Progression_Prediction():

    def __init__(self,age,sex,bmi,bp,s1,s2,s3,s4,s5,s6):
        """ init function for accepting the User Input """
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.bp = bp
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as file:
            self.model = pickle.load(file)

        with open(config.COLUMN_LIST__PATH,'r') as file:
            self.columns_dict = json.load(file)


    def Predict_Progression(self):
        self.load_model()

        array = np.zeros(len(self.columns_dict['columns']))

        array[0] = self.age
        array[1] = self.sex
        array[2] = self.bmi
        array[3] = self.bp
        array[4] = self.s1
        array[5] = self.s2
        array[6] = self.s3
        array[7] = self.s4
        array[8] = self.s5
        array[9] = self.s6
        # print(array)

        result = self.model.predict([array])   #this is normal predict model which is predine just
                                                #like in jupyter notebook 
        # print(result)

        return result[0]




if __name__ == '__main__':
    # km_driven = 120000.0
    # mileage = 19.7
    # engine = 796.0
    # max_power =46.3
    # seats = 5.0
    # brand_name = 'Maruti'
    # model = 'Alto'
    # seller = 'Dealer'
    # fuel = 'Petrol'
    # transmission = 'Manual' 
    # year= 2015


    Progression_Prediction_obj = Progression_Prediction(self,age,sex,bmi,bp,s1,s2,s3,s4,s5,s6)

    Progression_Prediction_obj.Predict_Progression()