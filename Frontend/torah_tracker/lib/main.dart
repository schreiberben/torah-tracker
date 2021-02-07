import 'package:flutter/material.dart';
import 'package:torah_tracker/assets/colors.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Torah Tracker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key key}) : super(key: key);

  @override
  _HomePage createState() => new _HomePage();
}

class _HomePage extends State<HomePage> with SingleTickerProviderStateMixin {
  TabController _tabController;
  List<Container> _tabs;

  _HomePage();

  @override
  void initState() {
    super.initState();
    _tabController = new TabController(vsync: this, length: 5);
    _tabs = _getTabs();
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      color: Colors.yellow,
      home: SafeArea(
        child: new Scaffold(
          body: Stack(children: <Widget>[
            TabBarView(
              controller: _tabController,
              children: _tabs.map((Container tab) {
                return new Center(child: tab);
              }).toList(),
            ),
          ]),
          appBar: AppBar(
              elevation: 5,
              toolbarHeight: 200,
              title: new TabBar(
                controller: _tabController,
                tabs: _tabs,
                labelStyle: TextStyle(fontSize: 70, color: Colors.red),
                unselectedLabelStyle:
                    TextStyle(fontSize: 30, color: Colors.blue),
                indicatorSize: TabBarIndicatorSize.label,
                indicatorColor: Colors.transparent,
                isScrollable: true,
              ),
              backgroundColor: titleBarColor,
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.only(
                      bottomLeft: Radius.elliptical(90, 40),
                      bottomRight: Radius.elliptical(90, 40)))),
          extendBodyBehindAppBar: true,
        ),
      ),
    );
  }

  List<Container> _getTabs() {
    List<String> names = ['תנ"ך', 'משנה', 'תלמוד', 'רמב"ם', 'שו"ע'];
    List<Container> outList = [];
    for (var i = 4; i >= 0; i--) {
      outList.add(Container(
        width: 200,
        height: 100,
        child: Tab(text: names[i]),
      ));
    }
    return outList;
  }
}
