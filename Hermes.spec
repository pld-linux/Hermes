Summary:	HERMES pixel format conversion library
Summary(pl):	HERMES - biblioteka konwersji formatów pixeli
Name:		Hermes
Version:	1.2.5
Release:	1
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://hermes.terminal.at/Hermes-%{version}.tar.gz
URL:		http://hermes.terminal.at/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HERMES is a library designed to convert a source buffer with a specified 
pixel format to a destination buffer with possibly a different format at
the maximum possible speed.

On x86 and MMX architectures, handwritten assembler routines are taking over
the job and doing it lightning fast.

On top of that, HERMES provides fast surface clearing, stretching and some
dithering. Supported platforms are basically all that have an ANSI C
compiler as there is no platform specific code but those are supported: DOS,
Win32 (Visual C), Linux, FreeBSD (IRIX, Solaris are on hold at the moment)

%description -l pl
HERMES jest bibliotek± do konwersji miêdzy ró¿nymi formatami buforów
pixeli z maksymaln± mozliw± szubkosci±.

Na procesorach x86 z architektur± MMX, procedury assemblerowe umo¿liwiaj±
bibliotece du¿± szybko¶æ dzia³ania.

HERMES umozliwia wype³nianie powierzchni, skalowanie i czê¶ciowo dithering.
HERMES mo¿e dzia³aæ na wszystkich platformach na które dostêpny jest
kompilator ANSI C, w tej chwili kod dostêpny jest dla DOS, Win32, Linux
FreeBSD.

%package devel
Summary:	HERMES header files and docementation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki HERMES
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and docementation for develp applications using HERMES library.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja potrzebne przy tworzeniu aplikacji
u¿ywaj±cych biblioteki HERMES.

%package static
Summary:	HERMES satic library
Summary(pl):	Biblioteka statyczna HERMES
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
HERMES satic library.

%description -l pl static
Biblioteka statyczna HERMES.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -g"; export CFLAGS
%configure \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix="$RPM_BUILD_ROOT%{_prefix}" install-strip

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

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
%attr(755,root,root) %{_libdir}/libHermes.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Fri Jun  4 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.5-1]
- added -g to CFLAGS (static librariest must be with debug info).

* Tue Apr 20 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.4-2]
- added - q %setup parameter,
- added devel and static subpackages,
- changed Group for main package,
- gzipping %doc,
- added "rm -rf $RPM_BUILD_ROOT" on top %install,
- added stripping shared libraries.

* Mon Apr 19 1999 Konrad Stepieñ <kornad@interdata.com.pl>
  [1.2.4-1]
- initial version
