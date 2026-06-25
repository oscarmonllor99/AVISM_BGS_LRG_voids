import numpy as np

def read_void_catalogue(filepath='', output_format = 'dictionaries'):
    """
    Reads the void_catalogue_clean.txt (ASCII) files, containing the cleaned void catalogue of AVISM.
    """

    #Check output format
    if output_format not in ['dictionaries', 'arrays']:
        raise ValueError('output_format must be "dictionaries" or "arrays"')

    with open(filepath, 'r') as void_catalogue:
        nvoids = int(void_catalogue.readline())
        #header
        void_catalogue.readline()
        voids=[]
        for iv in range(nvoids):
            void = {}
            data_line = np.array(void_catalogue.readline().split()).astype('f4')
            void['id'] = int(data_line[0])
            void['xc'] = data_line[1]
            void['yc'] = data_line[2]
            void['zc'] = data_line[3]
            void['gxc'] = data_line[4]
            void['gyc'] = data_line[5]
            void['gzc'] = data_line[6]
            void['vol'] = data_line[7]
            void['R'] = data_line[8]
            void['mean_overdensity'] = data_line[9]
            void['ellipticity'] = data_line[10]
            void['inv_porosity'] = data_line[11]
            voids.append(void)

        if output_format=='arrays':
            voids_arr = {k: np.array([v[k] for v in voids]) for k in voids[0].keys()}

    return voids_arr if output_format=='arrays' else voids