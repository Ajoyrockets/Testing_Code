import math as ms
import numpy as np
import simpy 

NUM_EMPLOYEES = 2
AVERAGE_SUPPORT_TIME = 10
CUSTOMER_INTEVAL = 2
SIM_TIME = 120

customer_handled = 0 

class CallCenter:

    def __init__(self, env, num_employees, support_time):
        self.env = env
        self.employee = simpy.Resource(env, num_employees)
        self.support_time = support_time
       
    def support(self,customer):
        random_time = max(1, np.random.normal(self.support_time))