Summary:	HERMES pixel format conversion library
Summary(pl.UTF-8):   HERMES - biblioteka konwersji grafiki rastrowej
Name:		Hermes
Version:	1.3.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.clanlib.org/~sphair/download/hermes/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	7dd49507a822b252ea8e3be8d0278d33
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.clanlib.org/hermes/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HERMES is a library designed to convert a source buffer with a
specified pixel format to a destination buffer with possibly a
different format at the maximum possible speed. On x86 and MMX
architectures, handwritten assembler routines are taking over the job
and doing it lightning fast. On top of that, HERMES provides fast
surface clearing, stretching and some dithering.

%description -l pl.UTF-8
HERMES jest biblioteką do konwersji między różnymi formatami buforów
pikseli z maksymalną możliwą szybkością. Na procesorach x86 z
architekturą MMX wstawki asemblerowe umożliwiają bibliotece dużą
szybkość działania. HERMES umożliwia wypełnianie powierzchni,
skalowanie i częściowo dithering.

%package devel
Summary:	HERMES header files and documentation
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do biblioteki HERMES
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentation for developing applications using
HERMES library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja potrzebne przy tworzeniu aplikacji
używających biblioteki HERMES.

%package static
Summary:	HERMES static library
Summary(pl.UTF-8):   Biblioteka statyczna HERMES
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
HERMES static library.

%description static -l pl.UTF-8
Biblioteka statyczna HERMES.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/api
%{_includedir}/Hermes
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
