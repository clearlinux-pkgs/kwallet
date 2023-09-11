#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kwallet
Version  : 5.110.0
Release  : 67
URL      : https://download.kde.org/stable/frameworks/5.110/kwallet-5.110.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.110/kwallet-5.110.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.110/kwallet-5.110.0.tar.xz.sig
Summary  : Secure and unified container for user passwords
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kwallet-bin = %{version}-%{release}
Requires: kwallet-data = %{version}-%{release}
Requires: kwallet-lib = %{version}-%{release}
Requires: kwallet-license = %{version}-%{release}
Requires: kwallet-locales = %{version}-%{release}
Requires: kwallet-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-xml
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : knotifications-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libgcrypt-dev
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : qca-qt5-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory consists of one daemon: kwalletd, and one library, in backend.
KWallet::Backend is used inside kwalletd to manage the actual files and
encryption.

%package bin
Summary: bin components for the kwallet package.
Group: Binaries
Requires: kwallet-data = %{version}-%{release}
Requires: kwallet-license = %{version}-%{release}

%description bin
bin components for the kwallet package.


%package data
Summary: data components for the kwallet package.
Group: Data

%description data
data components for the kwallet package.


%package dev
Summary: dev components for the kwallet package.
Group: Development
Requires: kwallet-lib = %{version}-%{release}
Requires: kwallet-bin = %{version}-%{release}
Requires: kwallet-data = %{version}-%{release}
Provides: kwallet-devel = %{version}-%{release}
Requires: kwallet = %{version}-%{release}

%description dev
dev components for the kwallet package.


%package lib
Summary: lib components for the kwallet package.
Group: Libraries
Requires: kwallet-data = %{version}-%{release}
Requires: kwallet-license = %{version}-%{release}

%description lib
lib components for the kwallet package.


%package license
Summary: license components for the kwallet package.
Group: Default

%description license
license components for the kwallet package.


%package locales
Summary: locales components for the kwallet package.
Group: Default

%description locales
locales components for the kwallet package.


%package man
Summary: man components for the kwallet package.
Group: Default

%description man
man components for the kwallet package.


%prep
%setup -q -n kwallet-5.110.0
cd %{_builddir}/kwallet-5.110.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694458700
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1694458700
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwallet
cp %{_builddir}/kwallet-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kwallet/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kwallet-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kwallet/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kwallet-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kwallet/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kwallet-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwallet/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kwallet-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kwallet/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kwallet-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwallet/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kwallet-query
%find_lang kwalletd5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kwallet-query
/V3/usr/bin/kwalletd5
/usr/bin/kwallet-query
/usr/bin/kwalletd5

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kwalletd5.desktop
/usr/share/dbus-1/interfaces/kf5_org.kde.KWallet.xml
/usr/share/dbus-1/services/org.kde.kwalletd5.service
/usr/share/knotifications5/kwalletd5.notifyrc
/usr/share/kservices5/kwalletd5.desktop
/usr/share/qlogging-categories5/kwallet.categories
/usr/share/qlogging-categories5/kwallet.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KWallet/KWallet
/usr/include/KF5/KWallet/kwallet.h
/usr/include/KF5/KWallet/kwallet_export.h
/usr/include/KF5/KWallet/kwallet_version.h
/usr/lib64/cmake/KF5Wallet/KF5WalletConfig.cmake
/usr/lib64/cmake/KF5Wallet/KF5WalletConfigVersion.cmake
/usr/lib64/cmake/KF5Wallet/KF5WalletTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Wallet/KF5WalletTargets.cmake
/usr/lib64/libKF5Wallet.so
/usr/lib64/libkwalletbackend5.so
/usr/lib64/qt5/mkspecs/modules/qt_KWallet.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Wallet.so.5.110.0
/V3/usr/lib64/libkwalletbackend5.so.5.110.0
/usr/lib64/libKF5Wallet.so.5
/usr/lib64/libKF5Wallet.so.5.110.0
/usr/lib64/libkwalletbackend5.so.5
/usr/lib64/libkwalletbackend5.so.5.110.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwallet/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kwallet/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kwallet/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwallet/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kwallet/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/kwallet-query.1

%files locales -f kwallet-query.lang -f kwalletd5.lang
%defattr(-,root,root,-)

