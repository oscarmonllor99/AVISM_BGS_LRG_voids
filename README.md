
## About and citation
Study carried out at the Departament d'Astronomia i Astrofísica of Universitat de València by Óscar Monllor-Berbegal in collaboration with Susana Planelles and Vicent Quilis. This work has been supported by Agencia Estatal de Investigación Española (AEI; grant PID2022-138855NB-C33) and by the Generalitat Valenciana (grant PROMETEO CIPROM/2022/49). Óscar Monllor-Berbegal acknowledges support from Universitat de València through an Atracció de Talent fellowship.

Citation: _Monllor-Berbegal et al. 2026_

## Clarification

Although AVISM recovers the full 3D shape of voids, the catalogues provided in this repository do not contain the 3D data arrays on which the irregular shapes and physical variables (density and velocity divergence) are saved, mainly because of their large size (1.5 GB each). Such data will be provided upon request. The simplified catalogue we provided here, therefore, can be used as a standalone spherical void catalogue or complemented with the more complex and rich 3D information.

## Catalogue description

We release the ASCII clean catalogues (`BGS_voids_clean.txt` and `LRG_voids_clean.txt`) after cleaning the raw catalogue provided as output by the [AVISM](https://github.com/oscarmonllor99/AVISM/) code when applied to the BGS and LRG galaxies of the DESI survey in the Data Release 1. To translate the angular and redshift positions to the 3D Cartesian comoving positions, we assume the following cosmology: $\Omega_m = 0.31$, $\Omega_\Lambda = 0.69$, $H_0 = 67.8 \mathrm{km s^{-1} \mathrm{Mpc}^{-1}}$. The following cube slices constitute the final input volumes provided to the void finder (in units of cMpc):

-1200 < $x_\text{BGS}$ < 200,

-700  < $y_\text{BGS}$ < 700, 

 -200 < $z_\text{BGS}$  < 1200, 

for the BGS and

-2800 < $x_\text{LRG}$  < -1400, 

-700 <  $y_\text{LRG}$  < 700, 

-700 <  $z_\text{LRG}$  < 700,  

for the LRGs. These cubes are in line with the following redshift cuts: $0.1 < z < 0.3$ and $0.4 < z < 0.8$ for the BGS and LRGs, respectively.
 
Before applying the void finder, both galaxy samples were preprocessed in order to convert the redshift-space positions to real space by correcting linear and non-linear redshift-space distortions. Furthermore, a [PIZA](https://arxiv.org/abs/astro-ph/9602100)-based velocity reconstruction algorithm is applied to run the void finder with its full capabilities, hence using both geometrical (density) and dynamical (velocity) information.

Each of the ASCII catalogues has a header indicating the number of clean voids saved in it. Then, another header indicates the different data columns:

- ID / $X$ / $Y$ / $Z$ / $X_G$ / $Y_G$ / $Z_G$ / Vol / $R$ / $\overline{\Delta}$ / $\epsilon$ / IP 

corresponding to the ID, maximum divergence centre ($\mathrm{cMpc}$), volume-weighted geometrical centre ($\mathrm{cMpc}$), volume ($\mathrm{cMpc}^3$), radius ($\mathrm{cMpc}$), mean overdensity, ellipticity, and inverse porosity, respectively. Take into account that the overdensity is defined as $\Delta = 1 + \delta$ with $\delta$ the density contrast. Each row contains the information for a given void ID in the clean void samples.


## Reader

Since the catalogue we present here has been postprocessed according to the cleaning steps followed in _Monllor-Berbegal et al. 2026_, the default reader provided in the [AVISM](https://github.com/oscarmonllor99/AVISM/) repository won't work. In that regard, we provide a simplified version of the reader for this repository's results: `read_void_cat.py`.

## Figures

In the following image, we display voids identified in a thin slice of the BGS and LRG data cubes, represented by circles resulting from the intersection of the slice and the spheres with radius equal to each void's effective radius. The voids are overlaid on top of the density contrast field interpolated by the void finder in order to carry out the void identification process. To get a glance at the 3D complex shapes of voids, see _Monllor-Berbegal et al. 2026_.

![Voids displayed in spherical shape](/figures/voids.png)

The next figures display the distribution of ellipticities, inverse porosity, and mean density:

![Voids displayed in spherical shape](/figures/hists.png)

![Voids displayed in spherical shape](/figures/stat_rad.png)

