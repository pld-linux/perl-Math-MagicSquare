%include	/usr/lib/rpm/macros.perl
Summary:	Math-MagicSquare perl module
Summary(pl):	Modu³ perla Math-MagicSquare
Name:		perl-Math-MagicSquare
Version:	1.40
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-MagicSquare-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-MagicSquare perl module.

%description -l pl
Modu³ perla Math-MagicSquare.

%prep
%setup -q -n Math-MagicSquare-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/MagicSquare
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,HISTORY}.gz

%{perl_sitelib}/Math/MagicSquare.pm
%{perl_sitearch}/auto/Math/MagicSquare

%{_mandir}/man3/*
