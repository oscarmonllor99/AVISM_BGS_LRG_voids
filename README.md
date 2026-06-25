
## About and citation
Study carried out at the Departament d'Astronomia i Astrofísica of Universitat de València by Óscar Monllor-Berbegal in collaboration with Susana Planelles and Vicent Quilis. This work has been supported by Agencia Estatal de Investigación Española (AEI; grant PID2022-138855NB-C33) and by the Generalitat Valenciana (grant PROMETEO CIPROM/2022/49). Óscar Monllor-Berbegal acknowledges support from Universitat de València through an Atracció de Talent fellowship.

Citation: _Monllor-Berbegal et al. 2026_

## Catalogue description

We release the ASCII catalogues provided as output by the [AVISM](https://github.com/oscarmonllor99/AVISM/) code when applied to the BGS and LRG galaxies of the DESI survey in the Data Release 1. To translate the angular and redshift positions to the 3D Cartesian comoving positions, we assume the following cosmology: $\Omega_m = 0.31$, $\Omega_\Lambda = 0.69$, $H_0 = 67.8 \mathrm{km s^{-1} \mathrm{Mpc}^{-1}}$. The following cube slices constitute the final input volumes provided to the void finder (in units of cMpc):

-1200 < $x_\text{BGS}$ < 200,

-700  < $y_\text{BGS}$ < 700, 

 -200 < $z_\text{BGS}$  < 1200, 

for the BGS and

-2800 < $x_\text{LRG}$  < -1400, 

-700 <  $y_\text{LRG}$  < 700, 

-700 <  $z_\text{LRG}$  < 700,  

for the LRGs. These cubes are in line with the following redshift cuts: $0.1 < z < 0.3$ and $0.4 < z < 0.8$ for the BGS and LRGs, respectively.
 
Before applying the void finder, both galaxy samples were preprocessed in order to convert the redshift-space positions to real space by correcting linear and non-linear redshift-space distortions. Furthermore, a [PIZA](https://arxiv.org/abs/astro-ph/9602100)-based velocity reconstruction algorithm is applied to run the void finder with its full capabilities, hence using both geometrical (density) and dynamical (velocity) information.

We provide two folders: `BGS` and `LRG` both containing a `voids00001`, which corresponds to the ASCII catalogue. The following information can be encountered inside these files:

----------------------------------------------------------------------------------

* $N_\ell$ /  $\ell_{min}$ /  $\ell_{max}$  /  $N_x^0$ /  $N_Y^0$ /  $N_z^0$  /  $L$
  
   - $\ell$ / $N_{cubes}$ / $N_{voids}$ / $N_{\ell-1}$ / FF / $\langle  \rho \rangle$
     
      - ID / $X$ / $Y$ / $Z$ / $X_G$ / $Y_G$ / $Z_G$ / Vol / $R$ / $\overline{\rho}$ / $\epsilon$ / IP / ID($\ell-1$) / $R(\ell-1)$ / Mass
        
        .
        .
        .
        
        (for all voids at this level)

      .
      .
      .
     
      (for all levels)

---------------------------------------------------------------------------------- 

Below, we provide three tables (one for each type of information given in `voidsXXXXX`) describing all variables listed before:

| Run variable  | Description |
| ------------- | ------------- |
| $N_\ell$  |  Number of grid levels |
| $\ell_{min}$ and $\ell_{max}$ | Minimum and maximum grid levels  |
| $N_x^0$, $N_y^0$, $N_z^0$ | Coarse (minimum) grid size in each cartesian direction|
| $L$  | Size (in Mpc) of the box in which the particles or grid are defined |

| Level variable  | Description |
| ------------- | ------------- |
| $\ell$  | Which level  |
| $N_{cubes}$ | Number of cubes found by the first void-finding step  |
| $N_{voids}$ | Final number of voids after merging and post-processing |
| $N_{\ell-1}$  | Number of voids in the previous level (parent voids) |
| FF  | Volume filling fraction of voids at this grid level |
| $\langle  \rho \rangle$ | Mean density used to define the density contrast

| Void property  | Description |
| ------------- | ------------- |
| ID | Void ID, corresponding to the ID of the biggest cube belonging to it |
| $X$, $Y$, $Z$| Void centre coordinates, defined as the maximum divergence point|
| $X_G$, $Y_G$, $Z_G$| Void volume-weighed (geometrical) centre |
| Vol | Void total volume (in $\text{Mpc}^3$) |
| $R$ | Void effective radius (in $\text{Mpc}$)|
| $\overline{\rho}$ | Mean density (in mean volume density units) inside the void |
| $\epsilon$ | Void ellipticity |
| IP | Void inverse porosity |
| ID($\ell-1$) | If applicable, ID of parent void at level $\ell-1$ |
| $R(\ell-1)$ | If applicable, radius of parent void at level $\ell-1$|
| Mass | Mass inside the void (in $M_{\odot}$)|

Note that, in the case of handling galaxy surveys, the galaxy density contrast ($\delta_g$) cannot be directly related to the underlying matter density contrast ($\delta_m$) and, hence, the mass provided by the void finder will be inaccurate. Also, in a small fraction of all cases, for very small voids, the ellipsoidal fit may fail and provide an absurd value. In those pathological cases, a value of `-99.0` is provided in the catalogue. For the BGS and LRG runs of the AVISM void finder, we only used one level $\ell = 0$ with $\Delta x \approx 2.8 \mathrm{cMpc}$ of resolution. Hence, the `parent` quantities are all saved with `0` and should be ignored.
