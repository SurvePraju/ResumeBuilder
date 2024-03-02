import React from 'react';
import { LocationOn } from '@mui/icons-material';
import EmailIcon from '@mui/icons-material/Email';
import CallIcon from '@mui/icons-material/Call';
import WebAssetIcon from '@mui/icons-material/WebAsset';

export default function TemplateOne() {
    return (
        <div className='layout'>
            <div className='section-part-one'>
                <div className="personal-info">
                    <Name firstName="Prajwal" lastName="Surve" />
                    <Designation name="Python Developer" />
                    <PersonalInfo website="survepraju.github.io" contact="9146346867" email="survpraju99@gmail.com" location="Thane, Maharashtra" />
                </div>
                <div className="personal-skill">
                    <SubSection section="Skills" />
                    <List />
                </div>
            </div>
            <div className='section-part-two'>
                <AboutMe description="uvdfhbfjbfajhkjnfcnflvmal;ml;mdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd" />
                <SubSection section="Education" />
                <NormalText text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem atque laudantium iste obcaecati error odio odit! Iure, illo. Soluta possimus labore ipsa eaque accusamus, voluptatibus tenetur dicta voluptatem voluptates exercitationem?" />
                <SubSection section="WorkExperience" />
                <NormalText text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem atque laudantium iste obcaecati error odio odit! Iure, illo. Soluta possimus labore ipsa eaque accusamus, voluptatibus tenetur dicta voluptatem voluptates exercitationem?" />
                <SubSection section="Projects" />
                <NormalText text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem atque laudantium iste obcaecati error odio odit! Iure, illo. Soluta possimus labore ipsa eaque accusamus, voluptatibus tenetur dicta voluptatem voluptates exercitationem?" />

            </div>
        </div>
    )
}



function Name(props) {
    return (
        <div className='full-name'>
            <h2>{props.firstName}</h2>
            <h2>{props.lastName}</h2>
        </div>
    );
}

function Designation(props) {
    return (
        <div className='designation'>
            <span>{props.name}</span>
        </div >
    )
}


function SubSection(props) {
    return (
        <div>
            <span>{props.section}</span>
        </div>
    )
}

function NormalText(props) {
    return (
        <span className='normal-text'>{props.text}</span>
    )
}

function List(props) {
    const allSkills = ["Python", "Django", "Flask", "MySql", "PostgreSql", "HTML", "CSS", "Bootstrap", "React"];
    return (
        <ul>
            {allSkills.map((skill, index) => <li key={index}><NormalText text={skill} /></li>)}
        </ul>
    )
}


function PersonalInfo(props) {
    const data = [
        { icon: <LocationOn sx={{ fontSize: 10 }} />, text: props.location },
        { icon: <EmailIcon sx={{ fontSize: 10 }} />, text: props.email },
        { icon: <CallIcon sx={{ fontSize: 10 }} />, text: props.contact },
        { icon: <WebAssetIcon sx={{ fontSize: 10 }} />, text: props.website }
    ];

    return (
        <div className='personal-info-subsection'>
            {data.map((item, index) => (
                <span key={index} className='block-inline'>
                    {item.icon} <NormalText text={item.text} />
                </span>
            ))}
        </div>
    );
}


function Description(props) {
    return (
        <p className="description">{props.text}</p>
    )
}

function AboutMe(props) {
    return (<><SubSection section="About Me" />
        <Description text={props.description} /></>)
}