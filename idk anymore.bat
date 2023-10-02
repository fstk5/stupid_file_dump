echo "Installing PyArmor..."
pip install pyarmor
echo "Encrypting file with PyArmor..."
pyarmor gen --private --enable-rft --enable-bcc --enable-jit --enable-themida --assert-call --obf-code 2 yp.py