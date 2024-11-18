#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: e822d6e
#
Name     : pesign
Version  : 116
Release  : 13
URL      : https://github.com/rhboot/pesign/releases/download/116/pesign-116.tar.bz2
Source0  : https://github.com/rhboot/pesign/releases/download/116/pesign-116.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pesign-bin = %{version}-%{release}
Requires: pesign-libexec = %{version}-%{release}
Requires: pesign-license = %{version}-%{release}
Requires: pesign-man = %{version}-%{release}
BuildRequires : mandoc
BuildRequires : nspr-dev
BuildRequires : pkgconfig(efivar)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(uuid)
BuildRequires : popt-dev
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-remove-root-check.patch
Patch2: clear-crash-patch.patch
Patch3: backport-fix-segfault.patch

%description
# pesign + efikeygen
Signing tools for PE-COFF binaries.  Compliant with the PE and Authenticode
specifications.

%package bin
Summary: bin components for the pesign package.
Group: Binaries
Requires: pesign-libexec = %{version}-%{release}
Requires: pesign-license = %{version}-%{release}

%description bin
bin components for the pesign package.


%package doc
Summary: doc components for the pesign package.
Group: Documentation
Requires: pesign-man = %{version}-%{release}

%description doc
doc components for the pesign package.


%package libexec
Summary: libexec components for the pesign package.
Group: Default
Requires: pesign-license = %{version}-%{release}

%description libexec
libexec components for the pesign package.


%package license
Summary: license components for the pesign package.
Group: Default

%description license
license components for the pesign package.


%package man
Summary: man components for the pesign package.
Group: Default

%description man
man components for the pesign package.


%prep
%setup -q -n pesign-116
cd %{_builddir}/pesign-116
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731946708
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1731946708
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pesign
cp %{_builddir}/pesign-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pesign/4cc77b90af91e615a64ae04893fdffa7939db84c || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/authvar
/usr/bin/efikeygen
/usr/bin/pesigcheck
/usr/bin/pesign
/usr/bin/pesign-client
/usr/bin/pesum

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pesign/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/pesign/pesign-authorize
/usr/libexec/pesign/pesign-rpmbuild-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pesign/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/authvar.1
/usr/share/man/man1/efikeygen.1
/usr/share/man/man1/pesigcheck.1
/usr/share/man/man1/pesign-client.1
/usr/share/man/man1/pesign.1
