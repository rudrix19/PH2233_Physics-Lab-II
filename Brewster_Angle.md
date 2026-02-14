# Determination of Refractive Index by Brewster Angle Method

## Aim of the Experiment
To determine the refractive index of a transparent material (microscope glass slide) by measuring the Brewster angle.

## Idea behind the Experiment
When an electromagnetic wave is incident on the interface between two dielectric media, part of the wave is reflected, and part is transmitted (refracted). The behaviour of light at such an interface is governed by Maxwell’s equations and the electromagnetic boundary conditions at the surface.

For an incident beam, the electric field vector can be resolved into two mutually perpendicular polarisation components:

- **s-polarised (perpendicular)**: Electric field perpendicular to the plane of incidence.  
- **p-polarised (parallel)**: Electric field parallel to the plane of incidence.  

Since the boundary conditions affect these components differently, their reflection and transmission coefficients differ.

---

### Fresnel Reflection and Brewster’s Law

According to the Fresnel equations, the amplitude reflection coefficient for the p-polarised component becomes zero at a specific angle of incidence known as the **Brewster angle ($θ_B$)**.

At this angle:

- The reflected light is completely **s-polarised**.
- The reflected and refracted rays are mutually perpendicular.
- The reflected p-component vanishes.

From Snell’s law:

$$n_1 \sin\theta_B = n_2 \sin\theta_t$$

At Brewster’s angle, the reflected and refracted rays are perpendicular:

$$\theta_B + \theta_t = 90^\circ$$

Substituting \( \theta_t = 90^\circ - \theta_B \) into Snell’s law:

$$n_1 \sin\theta_B = n_2 \cos\theta_B$$

$$\tan\theta_B = \frac{n_2}{n_1}$$

For light incident from air ($n_1 \approx 1$) onto a transparent material of refractive index \( n \):

$$\tan\theta_B = n$$

Thus, the refractive index of the material can be determined by measuring the Brewster angle.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9cd6bd35-4cae-4b23-8b70-74ed54fa3b24" alt="BrewsterAngle">
</p>

---

### Physical Interpretation

At Brewster’s angle, the induced dipoles in the material oscillate in a direction parallel to the transmitted beam. An oscillating dipole does not radiate along its axis of oscillation; therefore, no p-polarised light is reflected. As a result, the reflected light is purely s-polarised.

---

### Experimental Relevance

In this experiment, monochromatic light is incident on the surface of a transparent microscope glass slide. The reflected intensity is observed as the angle of incidence is varied. The angle at which the reflected intensity of the p-polarised component becomes minimum (ideally zero) is identified as the Brewster angle \( \theta_B \).

Using the relation:

$$n = \tan\theta_B$$

The refractive index of the material is calculated.

## Observations
<div align="center">

### Table 1: Variation of Reflected Photocurrent with Incident Angle

| Incident Angle (°) | I₁ (μA) | I₂ (μA) | I₃ (μA) | I₄ (μA) | I₅ (μA) | μI (μA) | σI (μA) |
|:------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| 10 | 42.0 | 67.1 | 91.0 | 69.4 | 70.2 | 67.94 | 24.51 |
| 15 | 40.1 | 71.2 | 96.0 | 100.0 | 90.1 | 79.48 | 27.98 |
| 20 | 39.5 | 69.8 | 58.6 | 90.0 | 80.5 | 67.68 | 15.23 |
| 25 | 46.4 | 65.6 | 52.8 | 63.0 | 60.4 | 57.64 | 9.86 |
| 30 | 47.7 | 44.8 | 39.3 | 47.7 | 45.8 | 45.06 | 4.25 |
| 35 | 35.8 | 39.1 | 37.6 | 43.2 | 40.3 | 39.20 | 1.67 |
| 40 | 23.2 | 22.4 | 24.7 | 29.8 | 25.6 | 25.14 | 1.16 |
| 45 | 11.6 | 13.4 | 12.3 | 11.7 | 10.9 | 11.98 | 0.91 |
| 50 | 5.5 | 4.6 | 4.4 | 5.2 | 4.8 | 4.90 | 0.59 |
| 55 | 0.4 | 0.4 | 0.5 | 1.1 | 0.6 | 0.60 | 0.06 |
| 60 | 1.6 | 1.8 | 2.4 | 2.7 | 1.9 | 2.08 | 0.42 |
| 65 | 19.4 | 20.0 | 17.4 | 23.8 | 18.7 | 19.86 | 1.37 |
| 70 | 40.8 | 66.1 | 54.2 | 162.0 | 50.3 | 74.68 | 12.69 |

**Caption:** Measured reflected photocurrent (μA) at different angles of incidence.  
$μ_I$ represents the mean current of five trials, and $σ_I$ denotes the standard deviation.

</div>

<div align="center">

### Figure 1: Reflected Current vs Incident Angle

<img src="https://github.com/user-attachments/assets/83c1b74f-8621-443a-9f19-d0e4541200d5" width="571" height="455">

**Caption:** Variation of reflected photocurrent (μA) with angle of incidence (°).  
The minimum intensity occurs at approximately 55°, corresponding to the Brewster angle.

</div>

## Calculations
From the graph, we obtain $\theta_B=55\degree$
Using Brewster's Law, $\tan \theta_B=n \implies n=\tan 55\degree$

<div align="center">

> ${n=1.428}$

</div>

The standard (literature) refractive index of glass is approximately $n=1.5$ 

∴ % Error = $\frac{1.5-1.428}{1.5}$ × 100 = 4.8%

## Conclusion
The Brewster angle for the given microscope glass slide was determined experimentally from the variation of reflected photocurrent with incident angle. The minimum reflected intensity was observed at 55°, which corresponds to the Brewster angle. Using Brewster's law, the refractive index of the material was calculated to be:
$$n=1.428$$
Comparing this with the standard refractive index of glass (≈ 1.50), the percentage error was 4.8%. The result is reasonably close to the accepted value, confirming the validity of Brewster's law and the reliability of the experimental method.

## Discussion
A crucial aspect of this experiment was the controlled use of a polariser and an analyser, which ensured accurate identification of the Brewster angle.

The polariser was used to convert the initially unpolarised light from the source into plane-polarised light. For Brewster's law verification, the incident light must be predominantly p-polarised (with the electric field parallel to the plane of incidence). Only the p-polarised component undergoes zero reflection at the Brewster angle. If the incident beam contains a significant s-component, the reflected intensity will not reduce to a sharp minimum, thereby increasing experimental uncertainty.

The analyser, placed in the path of the reflected beam, served two essential purposes:

- At the Brewster angle, the reflected beam should be purely s-polarised. By rotating the analyser, the extinction (minimum intensity) condition confirms the polarisation of the reflected light.
- The analyser helps isolate the reflected polarisation component and suppress unwanted stray light or residual polarisation components. This improves the sharpness of the intensity minimum and allows more precise determination of the Brewster angle.
