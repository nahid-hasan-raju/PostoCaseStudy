'''
Parameters required for the code
'''
import os,sys

'''
Please add the following line in ~/.bashrc
export MNTR_BB_ROOT_DIR = <YOUR PROJECT ROOT>
'''

PROJECT_ROOT = os.environ['MNTR_BB_ROOT_DIR']
sys.path.append(PROJECT_ROOT)

LIB_PATH=PROJECT_ROOT+'/'+'lib/'
SRC_PATH=PROJECT_ROOT+'/'+'src/'
OUTPUT_PATH=PROJECT_ROOT+'/'+'output/'
PICKLE_PATH=PROJECT_ROOT+'/'+'pickles/'
DATA_PATH=PROJECT_ROOT+'/'+'data/'


PICKLE_FLAG=True
REFINE=True

B=100000
c=0.99

VIZ_PER_COVERAGE=20

ARTIFACT_EVAL=True

# Here: please choose the figure to regenerate
FIG='5(a)' # Choose from {3(a), 3(b), 3(c), 4(a), 4(b), 4(c), 4(d), 5(a), 5(b), 5(c), 5(d)}

if ARTIFACT_EVAL==False:
    

    # Jet
    PROBABILITY_LOG=11
    DT=0.01
    DELTA_STATE=0.002
    DELTA_LOG=0.02
else:
    if FIG=='4(a)':
        PROBABILITY_LOG=5
        DT=0.01
        DELTA_STATE=0.002
        DELTA_LOG=0.02
        print("Parameters set for fig. 4(a)")
    elif FIG=='4(b)':
        PROBABILITY_LOG=5
        DT=0.01
        DELTA_STATE=0.002
        DELTA_LOG=0.04
        print("Parameters set for fig. 4(b)")
    elif FIG=='4(c)':
        PROBABILITY_LOG=3
        DT=0.01
        DELTA_STATE=0.002
        DELTA_LOG=0.02
        print("Parameters set for fig. 4(c)")
    elif FIG=='4(d)':
        PROBABILITY_LOG=3
        DT=0.01
        DELTA_STATE=0.002
        DELTA_LOG=0.04
        print("Parameters set for fig. 4(c)")
    elif FIG=='3(a)' or FIG=='3(c)' or FIG=='3(b)':
        PROBABILITY_LOG=5
        DT=0.01
        DELTA_STATE=0.002
        DELTA_LOG=0.02
        print("Parameters set for fig. 3(a..c)")
    elif FIG=='5(a)':
        PROBABILITY_LOG=3
        DT=0.01
        DELTA_STATE=0.004
        DELTA_LOG=0.2
        print("Parameters set for fig. 5(a)")
    elif FIG=='5(b)':
        PROBABILITY_LOG=3
        DT=0.01
        DELTA_STATE=0.004
        DELTA_LOG=0.4
        print("Parameters set for fig. 5(b)")
    elif FIG=='5(c)':
        PROBABILITY_LOG=1
        DT=0.01
        DELTA_STATE=0.004
        DELTA_LOG=0.2
        print("Parameters set for fig. 5(c)")
    elif FIG=='5(d)':
        PROBABILITY_LOG=1
        DT=0.01
        DELTA_STATE=0.004
        DELTA_LOG=0.4
        print("Parameters set for fig. 5(d)")
    else:
        print("No such figures found!")
        exit(0)
    


# ==========================================
# AutMod System Parameters

AUTMOD_DT = 0.001  # time step for Euler integration
AUTMOD_TOTAL_TIME = 10.0  # total simulation time in seconds

AUTMOD_X0 = 0.5  # initial x position
AUTMOD_Y0 = 0.5  # initial y position

AUTMOD_LOG_PROBABILITY = 0.2  # probability of logging each time step (0.2 = 20%)
AUTMOD_NOISE_STD = 0.05  # standard deviation of Gaussian measurement noise

AUTMOD_X_LIMIT = 3.0  # maximum absolute x value
AUTMOD_Y_LIMIT = 3.0  # maximum absolute y value
AUTMOD_MAX_DISTANCE = 5.0  # maximum distance from origin

AUTMOD_NUM_TRAJECTORIES = 4  # number of random trajectories to generate