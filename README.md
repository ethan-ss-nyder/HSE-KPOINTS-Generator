# HSE-KPOINTS-Generator
For use with VASP, these python scripts generate a KPOINTS file from given symmetry points compatible with HSE band structure calculations and clean up the EIGENVAL file from the resulting calculation.

HSEKPTGen.py:
Choice of symmetry points must be hard coded into the python script alongside number of points per line. Existing IBZKPT file must be placed in same directory as this script.
Procuces a KPOINTS file compatible with HSE band structure calculations.

HSEEigenCleaner.py:
Chosen k-point grid must be hard coded into the python script.
Edits k-point number and removes non-zero weighted k-point blocks in EIGENVAL file, making post-calclation analysis easier. By default, writes out an "EIGENVAL_OUT" file instead of overwriting EIGENVAL.

The combination of these two scripts greatly increases the efficiency of HSE band structure calculations using VASP.
