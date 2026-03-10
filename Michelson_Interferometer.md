# Michelson's Interferometer

## Aim of the Experiment
To determine the refractive index of a transparent material (microscope glass slide) by measuring the Brewster angle.

## Theory

A coherent monochromatic light source (typically a laser) is incident on a **partially silvered beam splitter**, which divides the beam into two parts. One part is reflected toward mirror **M₁**, while the other is transmitted toward mirror **M₂**. After reflection from the mirrors, the beams return to the beam splitter, where they recombine and interfere. The resulting interference pattern of bright and dark fringes is observed on a screen or detector.

<p align="center">
  <img src="https://github.com/user-attachments/assets/488a27a1-7ee5-4744-863b-c3c8f7a9e102" width="700">
</p>

If the optical paths of the two beams differ by an integer multiple of the wavelength, **constructive interference** occurs and a bright fringe is observed. If the path difference equals an odd multiple of half the wavelength, **destructive interference** occurs, producing a dark fringe.

When one of the mirrors (usually M₁) is displaced by a small distance `d`, the optical path difference between the two beams changes by **twice the displacement**, because the beam travels the distance twice (forward and backward). As the mirror moves, the interference pattern shifts and fringes move across the field of view.

Each time the optical path difference changes by one wavelength, one fringe passes the reference point.

Thus, if `N` fringes pass when the mirror is displaced by distance `d`, the wavelength of the light is given by

$$\lambda = \frac{2d}{N}$$

If the displacement is measured using a micrometer screw gauge with calibration constant `δ`, the expression becomes

$$\lambda = \frac{2d}{N} \times \delta$$

where:

- `λ` = wavelength of the laser light  
- `d` = measured mirror displacement  
- `N` = number of fringes shifted 
- `δ` = micrometer calibration constant  

---

### Determination of the Refractive Index of Air

A sealed **air cell** of length `x` is placed in one arm of the interferometer. Initially the cell contains air at atmospheric pressure `P`. When the pressure inside the cell is changed by a small amount `ΔP`, the refractive index of air changes correspondingly.

Since the **optical path length** depends on the refractive index `n`, a change in `n` produces a change in the optical path difference between the two beams. As a result, the interference fringes shift.

The optical path length through a medium is given by

$$\text{Optical Path Length} = n \times d$$


When the refractive index changes, the optical path difference between the two interfering beams changes, causing `N` fringes to move across the field of view. From this fringe shift, the refractive index of air can be determined.

The relationship between the refractive index of air and the observed fringe shift is

$$N = \left(\frac{2d(n-1)}{\lambda}\right)\left(\frac{\Delta P}{P_0}\right)$$

where:

- `n` = refractive index of air  
- `d` = length of the air cell  
- `λ` = wavelength of the laser light  
- `$P0$` = atmospheric pressure  
- `ΔP` = change in pressure in the air cell  
