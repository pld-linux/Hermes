Summary:	HERMES pixel format conversion library
Summary(pl):	HERMES - biblioteka konwersji grafiki rastrowej
Name:		Hermes
Version:	1.3.0
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Development/Librairies
Group(pl):	Biblioteki
Source:		http://dark.x.dtu.dk/~mbn/clanlib/download/%{name}-%{version}.tar.gz
Patch0:		Hermes-DESTDIR.patch
Patch1:		Hermes-automake.patch
URL:		http://hermes.terminal.at/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HERMES is a library designed to convert a source buffer with a specified
pixel format to a destination buffer with possibly a different format at
the maximum possible speed.  On x86 and MMX architectures, handwritten
assembler routines are taking over the job and doing it lightning fast.  On
top of that, HERMES provides fast surface clearing, stretching and some
dithering.

%description -l pl
HERMES jest bibliotek� do konwersji mi�dzy r�nymi formatami bufor�w pixeli
z maksymaln� mo�liw� szybkosci�.  Na procesorach x86 z architektur� MMX
wstawki assemblerowe umo�liwiaj� bibliotece du�� szybko�� dzia�ania.
HERMES umo�liwia wype�nianie powierzchni, skalowanie i cz�ciowo dithering.

%package devel
Summary:	HERMES header files and docementation
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki HERMES
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and docementation for develp applications using HERMES
library.

%description -l pl devel
Pliki nag��wkowe i dokumentacja potrzebne przy tworzeniu aplikacji
u�ywaj�cych biblioteki HERMES.

%package static
Summary:	HERMES static library
Summary(pl):	Biblioteka statyczna HERMES
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
HERMES static library.

%description -l pl static
Biblioteka statyczna HERMES.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS CHANGES TODO TODO.conversion

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz docs/api
%{_includedir}/Hermes
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
