# Simulate Matern hard-core point processes (Type I/II) on a rectangle.
# Author: H. Paul Keeler, 2019.
# Website: hpaulkeeler.com
# Repository: github.com/hpaulkeeler/posts
# For more details, see the post:
# hpaulkeeler.com/simulating-matern-hard-core-point-processes/

import numpy as np # NumPy package for arrays, random number generation, etc
import matplotlib.pyplot as plt  # For plotting

if __name__ == "__main__":

    num_sim = 1
    # Simulation window parameters
    xMin = 0
    xMax = 2
    yMin = 0
    yMax = 1

    #Parameters for the parent and daughter point processes
    lambdaPoisson = 50#density of underlying Poisson point process
    radiusCore = 0.1#radius of hard core

    #Extended simulation windows parameters
    rExt=radiusCore #extension parameter -- use core radius
    xMinExt=xMin-rExt
    xMaxExt=xMax+rExt
    yMinExt=yMin-rExt
    yMaxExt=yMax+rExt
    #rectangle dimensions
    xDeltaExt=xMaxExt-xMinExt
    yDeltaExt=yMaxExt-yMinExt
    areaTotalExt=xDeltaExt*yDeltaExt #area of extended rectangle

    for ss in range(num_sim):
        
        #Simulate Poisson point process for the parents
        numbPointsExt= np.random.poisson(areaTotalExt*lambdaPoisson)#Poisson number
        #x and y coordinates of Poisson points for the parent
        xxPoissonExt=xMinExt+xDeltaExt*np.random.rand(numbPointsExt)
        yyPoissonExt=yMinExt+yDeltaExt*np.random.rand(numbPointsExt)
        
        #thin points if outside the simulation window
        booleWindow=((xxPoissonExt>=xMin)&(xxPoissonExt<=xMax)&(yyPoissonExt>=yMin)&(yyPoissonExt<=yMax))
        indexWindow=np.arange(numbPointsExt)[booleWindow]
        #retain points inside simulation window
        xxPoisson=xxPoissonExt[booleWindow]
        yyPoisson=yyPoissonExt[booleWindow]
        
        numbPoints=len(xxPoisson) #number of Poisson points in window
        #create random marks for ages
        
        ###START Removing/thinning points START###
        booleRemoveI=np.zeros(numbPoints, dtype=bool)#Index for removing points -- Matern I
        for ii in range(numbPoints):
            distTemp=np.hypot(xxPoisson[ii]-xxPoissonExt,yyPoisson[ii]-yyPoissonExt) #distances to other points        
            booleInDisk=(distTemp<radiusCore)&(distTemp>0)#check if inside disk
            
            #Matern I
            booleRemoveI[ii]=any(booleInDisk)
        ###END Removing/thinning points END###
        
        #Remove/keep points to generate Matern hard-core processes
        #Matérn I
        booleKeepI=~(booleRemoveI)
        xxMaternI=xxPoisson[booleKeepI]
        yyMaternI=yyPoisson[booleKeepI]

    ###END Simulations END####

    ##Plotting
    markerSize=12; #marker size for the Poisson points
    plt.plot(xxPoisson,yyPoisson, 'ko',markerfacecolor="None",markersize=markerSize)
    plt.plot(xxMaternI,yyMaternI, 'rx',markersize=markerSize/2)
    plt.legend(('Removed Poisson','Matern I'))

    #Compare statistics
    diskArea=np.pi*radiusCore**2 #area of disk
    areaWindow=(xMax-xMin)*(yMax-yMin) #area of simulation window

    #underlying Poisson point process
    plt.show()