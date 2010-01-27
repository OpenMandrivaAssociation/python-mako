Name: python-mako
Version: 0.2.5
Release: %mkrel 1
Summary: Mako template library for Python

Group: Development/Python 
License: MIT
URL: http://www.makotemplates.org/
Source0: http://www.makotemplates.org/downloads/Mako-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch
BuildRequires: python-setuptools
Requires: python-beaker

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.


%prep
%setup -q -n Mako-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README doc examples
%{_bindir}/mako-render
%{python_sitelib}/*
