#
# Conditional build:
# one test is completly broken
%bcond_with	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	MagicSquare
Summary:	Math::MagicSquare Perl module - magic square checker
Summary(pl):	Modu³ Perla Math::MagicSquare - sprawdzanie kwadratów magicznych
Name:		perl-Math-MagicSquare
Version:	2.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9d5b59f9c3a9a8419dc92b02b14d698
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The first purpose of this Perl module is to help you to check your
Square. Is it a Semimagic Square? Is it a Magic Square?

The second purpose of this Perl module is to help you to print your
Square. At the moment the method available is 'print' that prints the
square on STDOUT and 'printhtml' that prints the square in HTML
format.

The third purpose of this Perl module is to help you to manipulate
your Square. At the moment the available methods are 'rotation' that
rotates your Square of 90 degree clockwise and 'reflection' that
reflect your Square.

%description -l pl
Pierwszym celem tego modu³u Perla jest pomoc przy sprawdzaniu
kwadratów. Czy kwadrat jest semimagiczny? Czy jest magiczny?

Drugim celem jest pomoc przy wypisywaniu kwadratów. Aktualnie jest
dostêpna metoda 'print' wypisuj±ca kwadrat na standardowe wyj¶cie oraz
metoda 'printhtml' wypisuj±ca w formacie HTML.

Trzecim celem tego modu³u jest pomoc przy modyfikowaniu kwadratu.
Aktualnie dostêpna jest metoda 'rotation' obracaj±ca kwadrat o 90
stopni zgodnie z kierunkiem ruchu wskazówek zegara oraz metoda
'reflection' dokonuj±ca odbicia lustrzanego kwadratu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO HISTORY
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
