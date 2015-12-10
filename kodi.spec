%define branch_release Isengard
%define version	15.2
%define rel	1
%define ffmpeg_archive_name 2.6.4-Isengard

%define Werror_cflags %nil

Summary:	Kodi - media player and home entertainment system
Name:		kodi
Version:	%{version}
Release:	%mkrel %rel
Source:		http://mirrors.xbmc.org/releases/source/xbmc-%{version}-%{branch_release}.tar.xz
Source4:	ffmpeg-%{ffmpeg_archive_name}.tar.gz
Source10:	kodi.png
URL:		http://kodi.tv/
Patch214:       0001-Fix-handling-of-filenames-with-spaces-in-wrapper-she.patch
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
#-----------------------------------------
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gettext-devel
BuildRequires: gperf
BuildRequires: texi2html
BuildRequires: java-1.8.0-openjdk
BuildRequires: swig
BuildRequires: pkgconfig(yajl)
BuildRequires: yasm
BuildRequires: pkgconfig(zlib)
BuildRequires: zip
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcec)
BuildRequires:	crystalhd-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(cwiid)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(expat)
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(glew)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	lzo-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libmicrohttpd)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(nettle)
BuildRequires:	pkgconfig(libnfs)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:  pkgconfig(platform)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(python)
BuildRequires:	readline-devel
BuildRequires:	rtmp-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(libshairport)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	ssh-devel
BuildRequires:	tiff-devel
BuildRequires:	tinyxml-devel
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xvmc)

%ifarch %ix86
BuildRequires:	nasm
%endif
#-----------------------------------------
Requires:	lsb-release
Requires:	curl
Requires:	xdpyinfo
Requires:	glxinfo
Requires:	pygtk2
Requires:	python-imaging
Requires:	python-pybluez
Requires:	python-gobject
Requires:  	avahi-python
Requires: 	python-dbus
Requires:	glibc >= 2.20
#----------------------------------------
Obsoletes: xbmc < %version
Provides: xbmc = %version-%release
Obsoletes: xbmc-eventclient-j2me < %version
Obsoletes: xbmc-eventclient-ps3 < %version
Obsoletes: xbmc-eventclient-wiiremote < %version
Obsoletes: xbmc-eventclient-xbmc-send < %version
Obsoletes: xbmc-eventclients-common < %version
Provides: xbmc-eventclient-j2me = %version-%release
Provides: xbmc-eventclient-ps3 = %version-%release
Provides: xbmc-eventclient-wiiremote = %version-%release
Provides: xbmc-eventclient-xbmc-send = %version-%release
Provides: xbmc-eventclients-common = %version-%release
#----------------------------------------

%description
Kodi (formerly known as XBMC) is an award-winning free and open source
software media player and entertainment hub for digital media.

While Kodi functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, Kodi feels very natural to use from the couch and is the
ideal solution for your home theater.


%package	devel
Summary:	Development files for Kodi
Group:		Development/C
License:	GPLv2+
Obsoletes: xbmc-eventclients-devel < %version
Provides: xbmc-eventclients-devel = %version-%release

%description	devel
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build addons and eventclients.

%prep
%setup -q -n xbmc-%{version}-%{branch_release}
%patch214 -p1

# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -print -delete

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

#add ffmpeg source

tar xpfz %{SOURCE4} -C tools/depends/target/ffmpeg/
tar cpfz tools/depends/target/ffmpeg/ffmpeg-%{ffmpeg_archive_name}.tar.gz -C tools/depends/target/ffmpeg/ FFmpeg-%{ffmpeg_archive_name}/
rm -r tools/depends/target/ffmpeg/FFmpeg-%{ffmpeg_archive_name}


%build

export GIT_REV="tarball"
export PYTHON_VERSION=2

./bootstrap

%define _disable_ld_no_undefined 1

%configure \
    --disable-hal \
    --disable-debug \
    --disable-non-free \
    --disable-shared \
    --enable-dvdcss \
        --enable-goom \
        --with-pic \
        --enable-mid \
        --enable-vaapi \
        --enable-libbluray \
    --with-lirc-device=/var/run/lirc/lircd \
    --with-ffmpeg=force


%make
%make -C tools/EventClients wiimote 

    
%install
rm -rf %buildroot
%makeinstall_std
%makeinstall_std -C tools/EventClients

# unused
rm -f %{buildroot}%{_datadir}/xsessions/kodi.desktop
rm -f %{buildroot}%{_datadir}/xsessions/xbmc.desktop

#Menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Video" \
  --dir %{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/applications/*.desktop


install -d -m755 %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/15Kodi <<EOF
NAME=Kodi
ICON=%{name}.png
DESC=Kodi Media Center
EXEC=%{_bindir}/%{name}-standalone
SCRIPT:
exec %{_bindir}/%{name}-standalone
EOF

# unused files
find %{buildroot}%{_datadir}/%{name}/addons/skin.*/media -name '*.png' -delete

# remove compat directory symlinks (RPM cannot handle dir=>symlink transition so
# more complex handling would be needed for these)
rm %{buildroot}%{_datadir}/xbmc
rm %{buildroot}%{_libdir}/xbmc
rm %{buildroot}%{_includedir}/xbmc

# to see a icon in lxde startmenu
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 644 %SOURCE10 %{buildroot}%{_datadir}/pixmaps/kodi.png


%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_sysconfdir}/X11/wmsession.d/15Kodi
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
# compat
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/system
%dir %{_libdir}/%{name}/system/players
%dir %{_libdir}/%{name}/system/players/dvdplayer
#%dir %{_libdir}/%{name}/system/players/paplayer
%{_libdir}/%{name}/%{name}.bin
%{_libdir}/%{name}/%{name}-xrandr

%{_libdir}/%{name}/addons
%{_datadir}/%{name}/addons

%{_libdir}/%{name}/system/ImageLib-*-linux.so
%{_libdir}/%{name}/system/hdhomerun-*-linux.so
#%{_libdir}/%{name}/system/libcmyth-*-linux.so
%{_libdir}/%{name}/system/libcpluff-*-linux.so
%{_libdir}/%{name}/system/libexif-*-linux.so
%ifarch %ix86 x86_64
%{_libdir}/%{name}/system/libsse4-*-linux.so
%endif
%{_libdir}/%{name}/system/players/dvdplayer/*-linux.so

#%{_libdir}/%{name}/system/players/paplayer/libsidplay2-*-linux.so
#%{_libdir}/%{name}/system/players/paplayer/nosefart-*-linux.so
#%{_libdir}/%{name}/system/players/paplayer/stsoundlibrary-*-linux.so
#%{_libdir}/%{name}/system/players/paplayer/timidity-*-linux.so
#%{_libdir}/%{name}/system/players/paplayer/vgmstream-*-linux.so
%ifarch %ix86
#%{_libdir}/%{name}/system/players/paplayer/SNESAPU-*-linux.so
%endif
%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/FEH.py*
#%{_datadir}/%{name}/language
%{_datadir}/%{name}/media
#%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/system
%{_datadir}/%{name}/userdata
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%{_datadir}/pixmaps/kodi.png


%python_sitelib/%{name}
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png

%{_bindir}/%{name}-j2meremote
%{_bindir}/%{name}-ps3d
%{_bindir}/%{name}-ps3remote
%{_bindir}/%{name}-send
%{_bindir}/%{name}-wiiremote

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/%{name}/*.cmake

%clean
rm -rf %{buildroot}

%post
%make_session
/sbin/ldconfig

%postun
%make_session
/sbin/ldconfig


%changelog
