# Last News 2024-03-29

I recently got some support from my institution to continue the development of
this software and try to make it more usable to others. Therefore I'm currently
working on

1. separation of the software with demo
2. made a standalone binary that can be downloaded and launched for the three major platforms.

Stay tuned.

# About

This is the repository of a small application I made to teach with simple
interactive demonstrations or interactive figures.

The objectives are

- Simple or no API.
- Automatic creation of GUI control.
- No specific knowledge to create figure except python itself.
- Author is fully in charge of the demonstration code.
- Presentation in the classroom.
- Offline.

![demo.gif](demo.gif "Demo")

Looks the `demos` directory.

# Installation

The software is in unstable state and in development. At this time, I made it
for *my* needs only.

1. Clone the repository.
2. Install [poetry](https://python-poetry.org/).
3. In the root directory run `poetry install` to install dependencies.

After that you just have to launch it with `poetry run python3 teachapp.py`

# Authors

If you want to contribute, email me. If you use it, please cite me I, and link
to that page.

I'm François Orieux (http://pro.orieux.fr), an assistant professor,
Paris-Saclay University, in Laboratoire des Signaux et Systèmes.

# Copyright

Music : That Crooner from Nowhere - The Hudsucker is lost

# TODO

- Clean codebase and repository.

Long term

- win and osx support
- octave or matlab support
- web frontend (based on jupyter I suppose)

# Planned animatin

- continous convolution
- discrete convolution
- convolution of image
- Fourier synthesis (1D, 2D)
- Fourier properties animation
- Live spectrum
- C Order 1 system (LP, HP, BP)
- C Order 2 system
- C Order N system
- N Order 1 system
- N Order 2 system
- N Order N system

