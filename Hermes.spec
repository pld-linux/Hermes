Summary:	HERMES pixel format conversion library
Summary(pl):	HERMES - biblioteka konwersji formatów pixeli
Name:		Hermes
Version:	1.2.4
Release:	1
Copyright:	LGPL
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Source:		http://hermes.terminal.at/Hermes-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
URL:		http://hermes.terminal.at

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

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/
make

%install
make prefix="$RPM_BUILD_ROOT/usr" install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES TODO TODO.conversion docs/api
/usr/lib/libHermes.a
%attr(755,root,root) /usr/lib/libHermes.la
%attr(755,root,root) /usr/lib/libHermes.so.1.0.1
%attr(755,root,root) /usr/lib/libHermes.so.1
%attr(755,root,root) /usr/lib/libHermes.so
/usr/include/Hermes

%changelog

* Mon Apr 19 1999 Konrad Stepieñ <kornad@interdata.com.pl>
- initial version
