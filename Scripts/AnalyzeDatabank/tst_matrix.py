import numpy as np

tr_matrix = '/media/akiirikk/DATADRIVE1/tietokanta/NMRLipids_Databank/Databank/Data/TransitionMatrix/f40/bb6/f40bb6ab5d44402be07059e8df74b5a8200f031e/6774168dfec0a5a7377c8a46341eba603f320cf7/transition_matrix_bins100.txt'

matrix_file = '/media/akiirikk/DATADRIVE1/tietokanta/NMRLipids_Databank/Databank/Data/TransitionMatrix/f40/bb6/f40bb6ab5d44402be07059e8df74b5a8200f031e/6774168dfec0a5a7377c8a46341eba603f320cf7/tst.txt'

t_matrix = np.loadtxt(tr_matrix, usecols=range(100))
lt = 0
dt = 10
avg_box_z = 20
bins_to_txt_file = np.linspace(-0.5*avg_box_z, 0.5*avg_box_z, num=101, endpoint=True)
translate_by = bins_to_txt_file[50]
print(bins_to_txt_file)
print(translate_by)
exit()
#translated_edges = 
edges = np.array2string(bins_to_txt_file,separator=' ')
characters = '[]\n'
edges_cleaned = edges
for c in characters:
    edges_cleaned = edges_cleaned.replace(c, '')




header =  'lt    ' + str(lt) + '\n' + 'dt    ' + str(dt) + '\n' + 'dn   ??? \n' + 'edges   ' + edges_cleaned  + '\n'

np.savetxt(matrix_file,t_matrix,header=header,  fmt='%d')
