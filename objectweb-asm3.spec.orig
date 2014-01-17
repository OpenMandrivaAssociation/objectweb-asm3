%{?_javapackages_macros:%_javapackages_macros}
Name:           objectweb-asm3
Version:        3.3.1
Release:        8.0%{?dist}
Summary:        Java bytecode manipulation and analysis framework
License:        BSD
URL:            http://asm.ow2.org/
BuildArch:      noarch

Source0:        http://download.forge.ow2.org/asm/asm-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  ant
BuildRequires:  maven-local
# shade-jar utility used in this spec file needs this
BuildRequires:  objectweb-asm3

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n asm-%{version}
find -name *.jar -delete
%mvn_alias :asm-all org.eclipse.jetty.orbit:org.objectweb.asm

sed -i /Class-path/d archive/asm-xml.xml

# Our system version of asm always used BSN org.objectweb.asm for
# asm-all because that's what Eclipse bundle has.  Now upstream
# provides OSGi metadata with incompatible BSN, but we want to keep
# compatibility with existing Eclipse plugins, so we have to use the
# old BSN (org.objectweb.asm).
sed -i s/org.objectweb.asm.all/org.objectweb.asm/ archive/asm-all.xml

%build
%ant -Dobjectweb.ant.tasks.path= jar jdoc

mv output/dist/lib/all/* output/dist/lib/

# Fix artifactId in POMs for shaded artifacts
for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml asm-all; do
    cp output/dist/lib/${m}-%{version}.pom output/dist/lib/${m}-distroshaded-%{version}.pom
    %pom_xpath_set "pom:project/pom:artifactId" "${m}-distroshaded" \
                   output/dist/lib/${m}-distroshaded-%{version}.pom
done

# Fix inter-module dependecies in POMs for shaded artifacts
pushd output/dist/lib
for m in asm-analysis asm-commons asm-util; do
    %pom_remove_dep :asm-tree ${m}-distroshaded-%{version}.pom
    %pom_add_dep asm:asm-tree-distroshaded:3.3.1 ${m}-distroshaded-%{version}.pom
done
%pom_remove_dep :asm-util asm-xml-distroshaded-%{version}.pom
%pom_add_dep asm:asm-util-distroshaded:3.3.1 asm-xml-distroshaded-%{version}.pom

%pom_remove_dep :asm asm-tree-distroshaded-%{version}.pom
%pom_add_dep asm:asm-distroshaded:3.3.1 asm-tree-distroshaded-%{version}.pom
popd

for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml asm-all; do
    shade-jar org.objectweb.asm org.objectweb.distroshaded.asm output/dist/lib/${m}-%{version}.jar \
              output/dist/lib/${m}-distroshaded-%{version}.jar
    jar xf output/dist/lib/${m}-distroshaded-%{version}.jar META-INF/MANIFEST.MF
    sed -i /Bundle-/d META-INF/MANIFEST.MF
    jar ufM output/dist/lib/${m}-distroshaded-%{version}.jar META-INF/MANIFEST.MF
done

%install
%mvn_artifact output/dist/lib/asm-parent-%{version}.pom

for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml asm-all; do
    %mvn_artifact output/dist/lib/${m}-distroshaded-%{version}.pom \
                  output/dist/lib/${m}-distroshaded-%{version}.jar
    %mvn_artifact output/dist/lib/${m}-%{version}.pom \
                  output/dist/lib/${m}-%{version}.jar
done
%mvn_install -J output/dist/doc/javadoc/user

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-attrs:%{name}/asm-util:%{name}/asm-xml %{name}-processor true

%files -f .mfiles
%doc LICENSE.txt README.txt
%{_bindir}/%{name}-processor
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Dec 16 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-8
- Remove OSGi metadata from shaded JARs
- Resolves: rhbz#1043066

* Fri Dec 06 2013 Michal Srb <msrb@redhat.com> - 3.3.1-7
- Separate artifacts for shaded asm

* Thu Dec 05 2013 Michal Srb <msrb@redhat.com> - 3.3.1-6
- Fix provides

* Thu Dec 05 2013 Michal Srb <msrb@redhat.com> - 3.3.1-5
- Build also "distroshaded" JARs and install them

* Thu Dec  5 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-4
- Change asm-all BSN to org.objectweb.asm

* Tue Dec  3 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-3
- Install asm-parent POM

* Thu Nov 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-2
- Remove classpath from manifest
- Install %{name}-processor command

* Mon Nov 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-1
- Initial packaging
