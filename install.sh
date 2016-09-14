sudo apt-get install autoconf automake libtool nasm make pkg-config git
git clone https://github.com/mozilla/mozjpeg.git
cd mozjpeg
autoreconf -fiv
mkdir build
cd build/
sh ../configure
make