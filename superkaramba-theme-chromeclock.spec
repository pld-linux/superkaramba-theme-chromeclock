
%define		theme	ChromeClock

Summary:	superkaramba - ChromeClock theme
Summary(pl):	superkaramba - motyw ChromeClock
Name:		superkaramba-theme-%{theme}
Version:	1
Release:	1
License:	GPL
Group:		Themes
Source0:	12972-ChromeClock.tar.bz2
# Source0-md5:	3f4a478cc4112a2b95a340292c76e79c
URL:		http://www.kde-look.org/content/show.php?content=12972
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ChromeClock theme for superkaramba.

%description -l pl
Motyw ChromeClock do superkaramby.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ChromeClock
		
install ChromeClock/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ChromeClock
install ChromeClock/*.py $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ChromeClock
install ChromeClock/*.pyc $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ChromeClock
install ChromeClock/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ChromeClock

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/ChromeClock
%{_datadir}/themes/superkaramba/ChromeClock/*.png
%{_datadir}/themes/superkaramba/ChromeClock/*.theme
%{_datadir}/themes/superkaramba/ChromeClock/*.py
%{_datadir}/themes/superkaramba/ChromeClock/*.pyc
