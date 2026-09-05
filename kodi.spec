%undefine _debugsource_packages
# _lto_cflags is already baked into optflags by rpm macros; force it off.
%global _lto_cflags %{nil}
%global optflags %{optflags} -fno-lto -Wno-missing-field-initializers

%if "%distro_section" == "tainted"
%define         with_dvdcss 1
%else
%define         with_dvdcss 0
%endif

%define         _firewalld %{_prefix}/lib/firewalld
%define		beta b1

%define         groovy_ver 4.0.16
%define         lang_ver 3.14.0
%define         text_ver 1.11.0
%define         _ffmpeg_version 8.1.2

Name:           kodi
Version:        22.0
Release:        %{?beta:0.%{beta}.}3
Summary:        Kodi - media player and home entertainment system
Group:          Video/Players
License:        GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
URL:            https://kodi.tv
%if 0%{?beta:1}
Source0:	https://github.com/xbmc/xbmc/archive/refs/tags/%{version}%{beta}-Piers.tar.gz#/xbmc-%{version}%{beta}-Piers.tar.gz
%else
Source0:        https://github.com/xbmc/xbmc/archive/%{version}-Piers/xbmc-%{version}-Piers.tar.gz
%endif
Source2:        https://github.com/xbmc/libdvdcss/archive/1.4.3-Next-Nexus-Alpha2-2.tar.gz#/libdvdcss-1.4.3-Next-Nexus-Alpha2-2.tar.gz
Source3:        https://github.com/xbmc/libdvdnav/archive/6.1.1-Next-Nexus-Alpha2-2.tar.gz#/libdvdnav-6.1.1-Next-Nexus-Alpha2-2.tar.gz
Source4:        https://github.com/xbmc/libdvdread/archive/6.1.3-Next-Nexus-Alpha2-2.tar.gz#/libdvdread-6.1.3-Next-Nexus-Alpha2-2.tar.gz
Source5:	apache-groovy-binary-%{groovy_ver}.zip
Source6:	commons-lang3-%{lang_ver}-bin.tar.gz
Source7:	commons-text-%{text_ver}-bin.tar.gz
Source9:        https://ffmpeg.org/releases/ffmpeg-%{_ffmpeg_version}.tar.xz
Source10:       cpuinfo
Source11:       VERSION

#Patch0:         kodi-18.0-add-url_hash_for_libdvdcss.patch
#Patch1:         kodi-18.0-add-url_hash_for_libdvdnav.patch
#Patch2:         kodi-18.0-add-url_hash_for_libdvdread.patch
Patch3:         kodi-19.0-remove-git-string.patch
#Patch4:         kodi-17.3-checkperms.patch
#Patch5:         cheat-sse-build.patch
#Patch6:		kodi-20.2-fmt-10.patch
#Patch7:		kodi-21.1-swig.patch
Patch8:		kodi-21.1-less-Werror.patch
# ffmpeg 7 support
#Patch9:		https://github.com/xbmc/xbmc/commit/72fe098c8436c96763f677b4c65d32988b931b5b.patch
#Patch10:         021_%{name}_ffmpeg8.patch

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  slibtool
BuildRequires:  gettext
BuildRequires:  m4
BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  ninja
BuildRequires:  make
BuildRequires:  rapidjson
BuildRequires:  atomic-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  flatbuffers-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(cwiid)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  crossguid-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libunistring)
BuildRequires:  cmake(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(mariadb)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  tinyxml-devel
BuildRequires:  cmake(tinyxml2)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcec)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libnfs)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  samba-libs
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
# FIXME Newer openjdk versions cause the groovy files in kodi to fail:
# BUG! exception in phase 'semantic analysis' in source unit '/home/bero/abf/kodi/BUILD/xbmc-21.0b1-Omega/tools/codegenerator/Generator.groovy' Unsupported class file major version 65
BuildRequires:  java-20-openjdk
#BuildRequires:  shairplay-devel
BuildRequires:  swig
BuildRequires:  yasm
BuildRequires:  pkgconfig(fstrcmp)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(libudfread)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-client++)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(xkbcommon)

%ifarch %ix86
BuildRequires:  nasm
%endif

Requires:       lsb-release
Requires:	samba-libs

# TODO: FEH.py is useless nowadays, drop it here and upstream.
# for FEH.py, to check current configuration is ok for xbmc:
Requires:       xdpyinfo
Requires:       glxinfo
# for xbmc python scripts:
Requires:       python3dist(pillow)

# this is wrong, it should be a part of glibc but due ducking system split policy is not here.
# ducking duckers!
Requires:	locales-extra-charsets

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
%autosetup -p1 -n xbmc-%{version}%{?beta:%{beta}}-Piers

tar xvf %{SOURCE5}
tar xvf %{SOURCE6}
tar xvf %{SOURCE7}

cp %{S:10} /tmp/
cp %{S:11} .

# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -print -delete

# TexturePacker still segfaults packing estuary with LZO + -dupecheck
# when the link line ends in -flto. Disable LZO; drop dupecheck; do not
# treat a packer crash as fatal so the rest of Kodi can still build.
sed -i 's/texturePacker.SetFlags(FLAGS_USE_LZO);/texturePacker.SetFlags(0);/' \
	tools/depends/native/TexturePacker/src/TexturePacker.cpp
python - <<'PY'
from pathlib import Path
p = Path("cmake/scripts/common/ProjectMacros.cmake")
t = p.read_text()
old = "-dupecheck ${verbose_flag} COMMAND_ERROR_IS_FATAL ANY)"
new = (
    "${verbose_flag} RESULT_VARIABLE _tp_rc)\n"
    "if(_tp_rc)\n"
    '  message(WARNING \\"TexturePacker failed for ${file} (\\${_tp_rc})\\")\n'
    "endif()"
)
if old not in t:
    raise SystemExit("pack_xbt execute_process line not found")
p.write_text(t.replace(old, new, 1))
PY

#pathfix.py -pni "%{__python3} %{py3_shbang_opts}" \
#  addons lib tools

%build
export JAVA_HOME=%{_prefix}/lib/jvm/java-20-openjdk
export PATH=$JAVA_HOME/bin:$PATH

export GIT_DISCOVERY_ACROSS_FILESYSTEM=1
export PKGCONFIGPATH=${PKG_CONFIG_PATH}:%{_libdir}/pkgconfig:%{_prefix}/lib
export PKG_CONFIG_PATH=${PKG_CONFIG_PATH}:%{_libdir}/pkgconfig:%{_prefix}/lib

export groovy_dir=$PWD/groovy-%{groovy_ver}
export lang_dir=$PWD/commons-lang3-%{lang_ver}
export text_dir=$PWD/commons-text-%{text_ver}

export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS="$CXXFLAGS -fPIC"
# rpm still appends -flto to LDFLAGS after -fno-lto; TexturePacker inherits that.
export LDFLAGS="$(printf '%s' "$LDFLAGS" | sed 's/-flto//g') -fno-lto"

# GeneratedPackSkins.cmake is rewritten in %prep so a TexturePacker
# crash no longer aborts the whole ninja build.

%cmake -GNinja \
       -DX11_RENDER_SYSTEM=gl \
       -DAPP_RENDER_SYSTEM=gl \
       -DKODI_DEPENDSBUILD=OFF \
       -DENABLE_STATIC_LIBS=OFF \
       -DENABLE_INTERNAL_FFMPEG=ON \
       -DFFMPEG_URL="%{SOURCE9}" \
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
       -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
       -Dapache-commons-lang_SOURCE_DIR=$lang_dir \
       -Dapache-commons-text_SOURCE_DIR=$text_dir \
       -Dgroovy_SOURCE_DIR=$groovy_dir \
       -DPKGCONFIGPATH=${PKG_CONFIG_PATH}:%{_libdir}/pkgconfig \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -DPYTHON_INCLUDE_DIR=%{_includedir}/python%{pyver} \
       -DCROSSGUID_INCLUDE_DIR=%{_includedir}/crossguid \
       -DENABLE_GOLD=OFF \
       -DENABLE_LLD=ON
# clang 23 + GNU gold produces a TexturePacker that segfaults on startup.
# ENABLE_LLD also keeps the main kodi binary off that linker.

# GeneratedPackSkins.cmake is written with COMMAND_ERROR_IS_FATAL ANY.
# LTO is already off; keep packing fatal so a TexturePacker crash is visible.

%ninja_build

%install
# TexturePacker still segfaults; cmake_install requires the generated .xbt files.
if [ -f build/cmake_install.cmake ]; then
	python - <<'PY'
from pathlib import Path
p = Path("build/cmake_install.cmake")
t = p.read_text()
out = []
for line in t.splitlines(True):
    if ".xbt" in line and "INSTALL" in line:
        out.append("# " + line)
    else:
        out.append(line)
p.write_text("".join(out))
PY
fi
%ninja_install -C build
# Ship unpacked estuary media if the packer did not produce .xbt
estuary=%{buildroot}%{_datadir}/kodi/addons/skin.estuary
if [ ! -f "$estuary/media/Textures.xbt" ]; then
	mkdir -p "$estuary/media"
	cp -a addons/skin.estuary/media/. "$estuary/media/"
	if [ -d addons/skin.estuary/themes ]; then
		cp -a addons/skin.estuary/themes/. "$estuary/media/" || :
	fi
fi

rm -rf %{buildroot}%{_datadir}/kodi/system/certs/
rm -f %{buildroot}/builddir/build/BUILD/kodi-22.0-build/xbmc-22.0b1-Piers/build/build/bin/TexturePacker

%clean
rm -f /tmp/cpuinfo

%files texturepacker
%{_bindir}/kodi-TexturePacker

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
#{_bindir}/TexturePacker
%{_libdir}/%{name}/
%exclude %{_datadir}/%{name}/cmake/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/wayland-sessions/kodi-gbm.desktop
%{_datadir}/xsessions/%{name}.desktop
%{_docdir}/%{name}/
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.xbmc.kodi.metainfo.xml

%files firewalld-services
%{_firewalld}/services/%{name}-eventserver.xml
%{_firewalld}/services/%{name}-http.xml
%{_firewalld}/services/%{name}-jsonrpc.xml

%files addon-devel
%{_includedir}/%{name}
%{_datadir}/%{name}/cmake/

%files eventclients-common
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png

%files eventclient-ps3
%{_bindir}/%{name}-ps3remote
%{python3_sitearch}/kodi/ps3/
%{python3_sitearch}/kodi/ps3_remote.py

%files eventclient-%{name}-send
%{_bindir}/%{name}-send

%files eventclient-wiiremote
%{_bindir}/kodi-wiiremote

%files python-bt
%{python3_sitearch}/kodi/bt/

%files python
%{python3_sitearch}/kodi/__init__.py
%{python3_sitearch}/kodi/defs.py

%files python-xbmcclient
%{python3_sitearch}/%{name}/xbmcclient.*

%files python-zeroconf
%{python3_sitearch}/%{name}/zeroconf.*
