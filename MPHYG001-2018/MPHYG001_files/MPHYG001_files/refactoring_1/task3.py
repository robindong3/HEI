from argparse import ArgumentParser
from matplotlib import pyplot as plt
import numpy as np

class julia(object):
    
    def __init__(self, y_axis_lim, x_axis_lim, resolution):
        self.y_axis_lim=y_axis_lim
        self.x_axis_lim=x_axis_lim
        self.resolution=resolution

    def generate_data(self, A, x, y, resolution,zx,zy):
        initial_cond=True
        
        while initial_cond==True:
            zx_squared=zx*zx
            zy_squared=zy*zy
            if zx_squared+zy_squared>=4 or resolution<=1:
                initial_cond=False
            a=zx_squared-zy_squared-0.7
            zy=2.0*zx*zy+0.27015
            zx=a
            resolution -= 1

        A[y][x]=resolution
        

    def main(self):
        y_axis_lim=self.y_axis_lim
        x_axis_lim=self.x_axis_lim
        resolution=self.resolution
        A = np.zeros([y_axis_lim,x_axis_lim])   
        
        for x in range(x_axis_lim):
            for y in range(y_axis_lim):
                zx=1.5*(x-x_axis_lim/2)/(0.5*x_axis_lim)
                zy=1.0*(y-y_axis_lim/2)/(0.5*y_axis_lim)

                self.generate_data(A, x, y, resolution, zx, zy)
                
        plt.imshow(A)
        plt.savefig('Myplot11.png') #the order matters
        
if __name__ == "__main__":
    parser = ArgumentParser(description="Julia Pattern")
    parser.add_argument('y_axis_limit', type=int)
    parser.add_argument('x_axis_limit', type=int)
    parser.add_argument('resolution', type=int)
    arguments = parser.parse_args()
    #nargs='?' allows to use a default value if no arguments are given and const gives the dafault
    #value and type make sure the input are integers
    
    initial=julia(arguments.y_axis_limit, arguments.x_axis_limit, arguments.resolution)
    initial.main()