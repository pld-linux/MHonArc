%include	/usr/lib/rpm/macros.perl
Summary:	An Email-to-HTML converter
Summary(pl.UTF-8):	Konwerter Poczta->HTML
Name:		MHonArc
Version:	2.6.18
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.mhonarc.org/release/MHonArc/tar/%{name}-%{version}.tar.bz2
# Source0-md5:	c3eaec31467b3cc5bae751fb68080742
Patch0:		%{name}-FHS2.patch
URL:		http://www.mhonarc.org/
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
Requires:	perl-Unicode-MapUTF8
Requires:	perl-Unicode-String
Requires:	perl-modules >= 5.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.

%description -l pl.UTF-8
MHonArc to konwerter poczta->HTML napisany w Perlu. MHonArc pozwala na
archiwizowanie poczty w postaci stron HTML z indeksowaniem według
wątku. MHonArc wspiera MIME oraz łatwo przystosowuje się do wymagań
użytkownika.

%prep
%setup -q
%{__sed} -i -e 's,^#!.*bin/perl5\?,#!%{__perl},' $(grep -rl '^#!.*/bin/perl' .)
%patch0 -p1

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__perl} install.me \
	-batch \
	-nodoc \
	-manpath=%{_mandir} \
	-binpath=%{_bindir} \
	-libpath=%{_datadir}/%{name} \
	-root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc examples extras logo admin ACKNOWLG BUGS CHANGES RELNOTES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
