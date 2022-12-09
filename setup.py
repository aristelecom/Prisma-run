import os 
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('-pyv', type=str, required=False, help='python version por example python, python3 or py',default = 'python3')


args = parser.parse_args()


def run_setup( python_v:str ) -> None:
    print(
    ''' 


        | |   (_) |            / _|
        | |__  _| | _____  ___| |_ ___  _ __ _____   _____ _ __ 
        | '_ \| | |/ / _ \/ __|  _/ _ \| '__/ _ \ \ / / _ \ '__|
        | |_) | |   <  __/\__ \ || (_) | | |  __/\ V /  __/ |   
        |_.__/|_|_|\_\___||___/_| \___/|_|  \___| \_/ \___|_|  



    '''
)
    #os.chdir('./src')    

    # run etl process
    os.system(f'{python_v} main.py')
    os.chdir('echo ejecutando api')
    os.chdir('../api')
   
    # run api server
    subprocess.Popen([f'{python_v}','apiMain.py'])
    os.chdir('echo ejecutando front')
    os.chdir('../front')
    
    subprocess.Popen(['streamlit', 'run' ,'home.py'])

    
if __name__ == '__main__':
   run_setup(args.pyv)



