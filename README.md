# Exclusive-UPC-NLO

Exclusive vector meson production (J/ψ, Υ) at next-to-leading order in the dipole picture,
for protons and nuclei.

The NLO calculation and the original code are by Jani Penttala
([JaniPenttala/NLO_VM_production](https://github.com/JaniPenttala/NLO_VM_production)).
If you use this code, please cite:

- H. Mäntysaari and J. Penttala, *Exclusive heavy vector meson production at next-to-leading
  order in the dipole picture*, Phys. Lett. B 823 (2021) 136723,
  [arXiv:2104.02349](https://arxiv.org/abs/2104.02349)
- H. Mäntysaari and J. Penttala, *Complete calculation of exclusive heavy vector meson
  production at next-to-leading order in the dipole picture*, JHEP 08 (2022) 247,
  [arXiv:2204.14031](https://arxiv.org/abs/2204.14031)

## Dipole fits

The dipole amplitudes are in `cpp/data/`, with one config per fit in `cpp/config_files/`.

- **NLO fits to HERA data** (`dipole-<evolution>-<data>-<coupling>-<Y0>.dip`):
  KCBK, ResumBK and TBK evolution; fits to all HERA data (`hera`) or light quarks only
  (`lightq`); Balitsky + smallest-dipole (`bal+sd`) or parent-dipole (`parent`) running
  coupling; evolution starting at Y₀ = 0 or 4.61.

  G. Beuf, H. Hänninen, T. Lappi and H. Mäntysaari, Phys. Rev. D 102, 074028 (2020),
  [arXiv:2007.01645](https://arxiv.org/abs/2007.01645).

- **KCBK MAP fits** (`kcbk_2506.00487/`, configs `conf-*kcbk-map-*`): proton and Pb, with
  Bal+SD or parent-dipole running coupling, evolution starting at x₀ = 1.

  C. Casuga, H. Hänninen and H. Mäntysaari, Phys. Rev. D 112, 034003 (2025),
  [arXiv:2506.00487](https://arxiv.org/abs/2506.00487).

  Taken from [hejajama/nlobk_dipole_nucleus](https://github.com/hejajama/nlobk_dipole_nucleus),
  with the 4th header line set to Y₀ = 0.

For nuclei, the dipole is given at each impact parameter b = 0, 2, …, 30 GeV⁻¹
(`-b_dependent`, `-b_folder`) and integrated over b in the code.

## Build

Needs CMake, GSL and nlodisfit (AmplitudeLib), cloned and built in a folder `nlodisfit/`
next to this repository.

```bash
cd cpp
mkdir -p build && cd build
cmake .. && make
```

The program is `cpp/build/bin/NLO_amplitude`.

## Run

Choose the calculation at the bottom of `cpp/calculate_amplitudes.sh`, for example

```bash
calculate_amplitude "A208-kcbk-map-parent-0.00" "Q2" 0.01 50 1000 false true "upsilon" 2
```

(config, fixed Q² = 0.01, W from 50 to 1000 GeV, transverse only, Υ, accuracy level 2), then

```bash
cd cpp
./calculate_amplitudes.sh
```

Results are written to `cpp/output/`.
