#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pesign
Version  : 0.112
Release  : 5
URL      : https://github.com/rhboot/pesign/releases/download/0.112/pesign-0.112.tar.bz2
Source0  : https://github.com/rhboot/pesign/releases/download/0.112/pesign-0.112.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pesign-bin
Requires: pesign-doc
BuildRequires : nspr-dev
BuildRequires : pkgconfig(efivar)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(popt)
BuildRequires : pkgconfig(uuid)
BuildRequires : popt-dev
Patch1: pesign_link.patch
Patch2: clear-crash-patch.patch

%description
Signing tool for PE-COFF binaries, hopefully at least vaguely compliant with
the PE and Authenticode specifications.

%package bin
Summary: bin components for the pesign package.
Group: Binaries

%description bin
bin components for the pesign package.


%package doc
Summary: doc components for the pesign package.
Group: Documentation

%description doc
doc components for the pesign package.


%prep
%setup -q -n pesign-0.112
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1497396832
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1497396832
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/authvar
/usr/bin/efikeygen
/usr/bin/efisiglist
/usr/bin/pesigcheck
/usr/bin/pesign
/usr/bin/pesign-client
/usr/libexec/pesign/pesign-authorize-groups
/usr/libexec/pesign/pesign-authorize-users

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/pesign/*
%doc /usr/share/man/man1/*
