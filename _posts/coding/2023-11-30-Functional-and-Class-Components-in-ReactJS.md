---
layout: post
title: Functional and Class Components in ReactJS
date:  2023-11-30 12:34:56 +0000
categories: coding javascript reactjs
type: coding
---
{% highlight javascript %}
import React, { useState } from "react";
import ReactDOM from "react-dom/client";
{% endhighlight %}

{% highlight javascript %}
function FunctionalComponent(props) {
  const [bgColor, setBgColor] = useState(props.bgColor);

  return (
    <div style={{ backgroundColor: bgColor }}>
      <h1>Functional Component</h1>
      <input value={bgColor} onChange={(e) => setBgColor(e.target.value)} />
    </div>
  );
}
{% endhighlight %}

{% highlight javascript %}
class ClassComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { bgColor: props.bgColor };
  }

  render() {
    return (
      <div style={{ backgroundColor: this.state.bgColor }}>
        <h1>Class Component</h1>
        <input
          value={this.state.bgColor}
          onChange={(e) => this.setState({ bgColor: e.target.value })}
        />
      </div>
    );
  }
}
{% endhighlight %}

{% highlight javascript %}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <FunctionalComponent bgColor="orange" />
    <hr />
    <ClassComponent bgColor="cyan" />
  </>
);
{% endhighlight %}