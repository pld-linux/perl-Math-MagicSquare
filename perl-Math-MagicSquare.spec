%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	MagicSquare
Summary:	Math::MagicSquare - Magic Square Checker
Name:		perl-Math-MagicSquare
Version:	1.40
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The first purpose of this PERL module is to help you to check your Square.
Is it a Semimagic Square?  Is it a Magic Square?

The second purpose of this PERL module is to help you to print your
Square.  At the moment the method available is 'print' that prints the
square on STDOUT and 'printhtml' that prints the square in HTML format.

The third purpose of this PERL module is to help you to manipulate
your Square.  At the moment the available methods are 'rotation' that
rotates your Square of 90 degree clockwise and 'reflection' that reflect
your Square.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO HISTORY
%{perl_sitelib}/Math/MagicSquare.pm
%{_mandir}/man3/*
