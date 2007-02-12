Summary:	A heavily improved version of the old GIMP Plasma plug-in
Summary(pl.UTF-8):   Znacznie usprawniona wersja wtyczki Plasma z GIMP-a
Name:		gimp-plugin-plasma2
Version:	2.11
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://trific.ath.cx/Ftp//gimp/plasma/plasma2-%{version}.tar.bz2
# Source0-md5:	8a4cb3bab1756920ab2dadb4e32b79c5
URL:		http://trific.ath.cx/software/gimp-plugins/plasma2/
BuildRequires:	gimp-devel >= 1:2.2.0
Requires:	gimp >= 1:2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Plasma2 is a heavily improved version of an old GIMP plug-in Plasma by
Stephen Norris generating cloud-like images known as "the plasma
fractal".

Brief list of fixes and improvements against original Plasma:

- Several new generator options, including the possibility to generate
  original Fractint-like and Norris-like plasmas,
- Can generate tilable images (much better than Plasma +
  Make_seamless),
- Switching tilability on/off modifies the image only as little as is
  necessary to achieve desired effect,
- Can directly map to a gradient (better than Plasma +
  Map_to_gradient),
- Can do a gradient-remix map,
- Better handling of grayscale images (and is 3 times faster on them),
- Buttons to revert/reset settings.

%description -l pl.UTF-8
Plasma2 to znacznie usprawniona wersja wtyczki Plasma z GIMP-a
napisanej przez Stephena Norrisa, która tworzy podobne do chmur obrazy
znane jako "fraktale plazmowe".

Krótka lista poprawek i usprawnień w porównaniu z oryginalną wersją:

- Kilka nowych opcji generatora, włączając możliwość tworzenia
  oryginalnych Fractintowych i Norrisowych plazm,
- Możliwość tworzenia kafelkowalnych obrazów (dużo lepsza jakość niż
  Plasma + Make_seamless),
- Włączanie/wyłączanie kafelkowalności wprowadza do obrazu tylko
  zmiany potrzebne do osiągnięcia efektu,
- Możliwość bezpośredniego mapowania na gradient (dużo lepsza niż
  Plasma + Map_to_gradient),
- Możliwość robienia map gradient-remix,
- Lepsza obsługa obrazów w skali szarości (a także trzykrotne
  przyspieszenie operacji na nich),
- Przyciski powrotu/kasowania ustawień.

%prep
%setup -q -n plasma2-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} -DLOCALEDIR=\\\"\`\$(GIMPTOOL) --prefix\`/share/locale\\\" -DVERSION=\\\"\$(VERSION)\\\" -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install plasma2 $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_plugindir}/*
