%if "%distro_section" == "tainted"
%define         with_dvdcss 1
%else
%define         with_dvdcss 0
%endif

%define         _firewalld %{_prefix}/lib/firewalld

Name:           kodi
Version:        19.1
Release:        1
Summary:        Kodi - media player and home entertainment system
Group:          Video/Players
License:        GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
URL:            https://kodi.tv
Source0:        https://github.com/xbmc/xbmc/archive/%{version}-Matrix/xbmc-%{version}-Matrix.tar.gz
Source2:        https://github.com/xbmc/libdvdcss/archive/1.4.2-Leia-Beta-5.tar.gz#/libdvdcss-1.4.2-Leia-Beta-5.tar.gz
Source3:        https://github.com/xbmc/libdvdnav/archive/6.0.0-Leia-Alpha-3.tar.gz#/libdvdnav-6.0.0-Leia-Alpha-3.tar.gz
Source4:        https://github.com/xbmc/libdvdread/archive/6.0.0-Leia-Alpha-3.tar.gz#/libdvdread-6.0.0-Leia-Alpha-3.tar.gz

Source10:       cpuinfo
Source11:       VERSION

Patch0:         kodi-18.0-add-url_hash_for_libdvdcss.patch
Patch1:         kodi-18.0-add-url_hash_for_libdvdnav.patch
Patch2:         kodi-18.0-add-url_hash_for_libdvdread.patch
Patch3:         kodi-19.0-remove-git-string.patch
#Patch4:         kodi-17.3-checkperms.patch
Patch5:         cheat-sse-build.patch

BuildRequires:  autoconf
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(expat)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(cwiid)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  crossguid-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  flatbuffers-devel
BuildRequires:  cmake(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  rapidjson
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcec)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libnfs)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  sndio-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  graphviz
BuildRequires:  doxygen
BuildRequires:  egl-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(mariadb)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  giflib-devel
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  java-openjdk-headless
#BuildRequires:  shairplay-devel
BuildRequires:  swig
BuildRequires:  yasm
BuildRequires:  pkgconfig(fstrcmp)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(udfread)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wavpack)

%ifarch %ix86
BuildRequires:  nasm
%endif

Requires:       lsb-release

# TODO: FEH.py is useless nowadays, drop it here and upstream.
# for FEH.py, to check current configuration is ok for xbmc:
Requires:       xdpyinfo
Requires:       glxinfo
# for xbmc python scripts:
Requires:       python3dist(pillow)

Provides:       xbmc = %{version}-%{release}

%description
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

While Kodi functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, Kodi feels very natural to use from the couch and is the
ideal solution for your home theater.

%if %with_dvdcss
The tainted package contains support for DVDCSS.
%endif

%package        firewalld-services
Summary:        Firewall services for Kodi
Group:          Video/Players
License:        GPLv2+
BuildArch:      noarch
Requires(pre):  firewalld
Requires:       %{name} >= %{version}-%{release}

%description    firewalld-services
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the firewall services for Kodi.

%package        addon-devel
Summary:        Development files for Kodi
Group:          Development/C
License:        GPLv2+

%description    addon-devel
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build addons and eventclients.

%package        eventclients-common
Summary:        Common files for Kodi eventclients
Group:          Video/Players
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-python = %{version}-%{release}

%description    eventclients-common
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%package        eventclient-ps3
Summary:        PS3 eventclients for Kodi
Group:          Video/Players
License:        GPLv2+
Recommends:       python3dist(pybluez)
Requires:       %{name}-eventclients-common = %{version}-%{release}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:       python3dist(pygobject)
Requires:       python3dist(dbus-python)

%description    eventclient-ps3
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package        eventclient-wiiremote
Summary:        Wii Remote eventclient for Kodi
Group:          Video/Players
License:        GPLv3+
Requires:       %{name}-eventclients-common = %{version}-%{release}

%description    eventclient-wiiremote
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package        eventclient-%{name}-send
Summary:        PS3 eventclient for Kodi
Group:          Video/Players
License:        GPLv2+
Requires:       %{name}-eventclients-common = %{version}-%{release}

%description    eventclient-%{name}-send
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the %{name}-send eventclient.

%package        python-bt
Summary:        Bluetooth Python scripts for Kodi
Group:          Video/Players
License:        GPLv2+
Requires:       %{name} >= %{version}-%{release}
BuildArch:      noarch

%description    python-bt
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the bluetooth python scripts.

%package        python
Summary:        Common Python scripts for Kodi
Group:          Video/Players
License:        GPLv2+
Requires:       %{name} >= %{version}-%{release}
BuildArch:      noarch

%description    python
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the common python scripts for Kodi.

%package        python-xbmcclient
Summary:        XBMCClient Python scripts for Kodi
Group:          Video/Players
License:        GPLv2+
Requires:       %{name} >= %{version}-%{release}
BuildArch:      noarch

%description    python-xbmcclient
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the xbmcclient python scripts.

%package        python-zeroconf
Summary:        Zeroconf Python scripts for Kodi
Group:          Video/Players
License:        GPLv2+
Requires:       %{name} >= %{version}-%{release}
BuildArch:      noarch

%description    python-zeroconf
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the zeroconf python scripts.

%package        texturepacker
Summary:        Zeroconf Python scripts for Kodi
Group:          Video/Players
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}

%description    texturepacker
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Texturepacker program for Kodi.

%prep
%autosetup -p1 -n xbmc-%{version}-Matrix

cp %{S:10} /tmp/
cp %{S:11} .

# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -print -delete

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" \
  addons lib tools

%build
export GIT_DISCOVERY_ACROSS_FILESYSTEM=1
export PKGCONFIGPATH=${PKG_CONFIG_PATH}:%{_libdir}/pkgconfig:%{_prefix}/lib
export PKG_CONFIG_PATH=${PKG_CONFIG_PATH}:%{_libdir}/pkgconfig:%{_prefix}/lib

%cmake -GNinja \
       -DX11_RENDER_SYSTEM=gl \
       -DKODI_DEPENDSBUILD=OFF \
       -DENABLE_STATIC_LIBS=OFF \
       -DENABLE_INTERNAL_FFMPEG=OFF \
       -DENABLE_INTERNAL_FLATBUFFERS=OFF \
       -DENABLE_INTERNAL_FMT=OFF \
       -DENABLE_INTERNAL_CROSSGUID=OFF \
       -DENABLE_INTERNAL_FSTRCMP=OFF \
       -DENABLE_INTERNAL_DAV1D=OFF \
       -DENABLE_INTERNAL_LIBDVD=OFF \
       -DENABLE_INTERNAL_UDFREAD=OFF \
       -DENABLE_INTERNAL_GTEST=OFF \
       -DENABLE_EVENTCLIENTS=ON \
       -DENABLE_UDFREAD=ON \
       -DENABLE_LIRCCLIENT=ON \
       -DENABLE_CCACHE=OFF \
       -DENABLE_TESTING=OFF \
       -DWITH_FFMPEG=%{_prefix} \
       -DFFMPEG_PATH=%{_prefix} \
       -DENABLE_APP_AUTONAME=ON \
       -DFREETYPE_INCLUDE_DIR=%{_includedir}/freetype2 \
       -DGIT_VERSION="by %{_vendor}" \
       -DLIBDVD_LIBRARIES=%{_libdir} \
       -DLIBDVD_INCLUDE_DIRS=%{_includedir} \
%if %with_dvdcss
       -DLIBDVDCSS_URL=%{SOURCE2} \
       -DENABLE_DVDCSS=ON \
%else
       -DENABLE_DVDCSS=OFF \
%endif
       -DLIBDVDNAV_URL=%{SOURCE3} \
       -DLIBDVDREAD_URL=%{SOURCE4} \
       -DPKGCONFIGPATH=${PKG_CONFIG_PATH}:%{_libdir}/pkgconfig \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -DPYTHON_INCLUDE_DIR=%{_includedir}/python%{pyver} \
       -DCROSSGUID_INCLUDE_DIR=%{_includedir}/crossguid

%ninja_build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_datadir}/kodi/system/certs/

%clean
rm -f /tmp/cpuinfo

%files texturepacker
%{_bindir}/TexturePacker

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
%{_libdir}/%{name}/
%exclude %{_datadir}/%{name}/cmake/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/xsessions/%{name}.desktop
%{_docdir}/%{name}/
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/

%files firewalld-services
%{_firewalld}/services/%{name}-eventserver.xml
%{_firewalld}/services/%{name}-http.xml
%{_firewalld}/services/%{name}-jsonrpc.xml

%files addon-devel
%{_bindir}/JsonSchemaBuilder
%{_includedir}/%{name}
%{_datadir}/%{name}/cmake/

%files eventclients-common
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png

%files eventclient-ps3
%{_bindir}/%{name}-ps3remote
%{python3_sitelib}/%{name}/ps3/
%{python3_sitelib}/%{name}/__pycache__/ps3*
%{python3_sitelib}/%{name}/ps3_remote.*

%files eventclient-%{name}-send
%{_bindir}/%{name}-send

%files eventclient-wiiremote
%{_bindir}/kodi-wiiremote

%files python-bt
%{python3_sitelib}/%{name}/bt/

%files python
%{python3_sitelib}/%{name}/defs.*
%{python3_sitelib}/%{name}/__init__.*
%{python3_sitelib}/%{name}/__pycache__/__init*
%{python3_sitelib}/%{name}/__pycache__/defs*

%files python-xbmcclient
%{python3_sitelib}/%{name}/xbmcclient.*
%{python3_sitelib}/%{name}/__pycache__/xbmc*

%files python-zeroconf
%{python3_sitelib}/%{name}/zeroconf.*
%{python3_sitelib}/%{name}/__pycache__/zero*
