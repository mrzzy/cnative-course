import React from 'react';
import API from "./API.js";
import './App.css';

// component to display organisation
function OrgCard(props) {
    return (
        <div className="Org card" onClick={props.onClick}>
            <h3> { props.name } </h3>
            <img src={ props.logoUrl } alt="Logo" />
        </div>
    );
}

// component to display a list of organisation
class OrgList extends React.Component {
    constructor(props) {
        super(props);

        this.api = new API();
        this.state = {
            orgs: []
        };
    };

    // pull list of orgs from the backend api
    async pullOrgs() {
        console.log("HERE");
        const orgIds = await this.api.query("org");
        var orgs = await Promise.all(
            orgIds.map(async (id) => {
                const org = await this.api.get("org", id) 
                org.id = id;
                return org;
            }));
    
        console.log(orgs);
        return orgs;
    }

    async componentDidMount() {
        const orgs = await this.pullOrgs();
        // rerender with orgs
        this.setState({
            "orgs": orgs
        });
    }

    onClick = async (orgId) => {
        await this.api.delete("org", orgId);
        window.location.reload();
    };

    render() {
        return (
            <div className="OrgList">
                { this.state.orgs.map((org) => (
                    <OrgCard key={org.id} name={org.name} logoUrl={org.logoUrl} 
                        onClick={ () => this.onClick(org.id) }/> )) }
            </div>
        );
    }
}

class OrgForm extends React.Component{
    constructor(props) {
        super(props);
        this.api = new API();
        this.state = {
            name: "",
            logoUrl: ""
        };
    }

    onChangeName = (event) => {
        this.setState({
            name: event.target.value
        });
    };

    onChangeLogo = (event) => {
        this.setState({
            logoUrl: event.target.value
        });
    };

    submit = async (event) => {
        event.preventDefault();
        const response = await this.api.create("org", this.state);
        window.location.reload();
    };

    render() {
        return (
            <form className="OrgForm" onSubmit={this.submit} >
                <div>
                    <label> Name: </label>
                    <input name="name" type="text" value={this.state.name}
                           onChange={this.onChangeName} />
                </div>

                <div>
                    <label> Logo: </label>
                    <input name="logoUrl" type="text" value={this.state.logoUrl} 
                           onChange={this.onChangeLogo} />
                </div>
                
                <button type="submit"> Create </button>
            </form>
        );
    }
}



function App() {
    return (
    <div className="App">
      <header className="App-header">
          Organisations
      </header>
      <main>
          <OrgList />
          <OrgForm />
      </main>
    </div>
    );
}

export default App;
